from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
import threading
import time
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

eyes = ['o ', ' o']
eye_index = 0

raspuns = ""
running = True
history = ""
MODEL_NAME = "stabilityai/stable-code-instruct-3b"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading model")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map={"": "cuda:0"}
)
# weird ass cat
def cat(eye):
    return "\n".join([
        "           .'\\   /`.",
        "         .'.-.`-'.-.`.",
        "    ..._:   .-. .-.   :_...",
        f"  .'    '-.({eye}) ({eye}).-'    `.",
        ":  _    _ _`~(_)~`_ _    _  :",
        ":  /:   ' .-=_   _=-. `   ;\\  :",
        ":   :|-.._  '     `  _..-|:   :",
        " :   `:| |`:-:-.-:-:'| |:'   :",
        " `.   `.| | | | | | |.'   .'",
        "    `.   `-:_| | |_:-'   .'",
        "      `-._   ````    _.-'",
        "          ``-------''"
    ])


# #   simulare LLM
# def llm(user_input):
#     global raspuns, running
#
#     if user_input.lower() == "exit":
#         running = False
#         return
#
#     # simulare răspuns
#     time.sleep(1)
#     raspuns = f"Pisica zice: {user_input[::-1]}"

def llm(user_input):
    global raspuns, running, history

    if user_input.lower() == "exit":
        running = False
        return
    raspuns = "Thinking..."
    prompt = history + f"\nUser: {user_input}\nAssistant:"

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")

    output = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    response = response.split("Assistant:")[-1].strip()

    history += f"\nUser: {user_input}\nAssistant: {response}"

    raspuns = response
#   thread input
def input_thread():
    while running:
        user_input = input(">>> ")
        threading.Thread(target=llm, args=(user_input,), daemon=True).start()


#   layout rich
layout = Layout()
layout.split_column(
    Layout(name="cat", size=15),
    Layout(name="response")
)


#   pornim input thread
threading.Thread(target=input_thread, daemon=True).start()


#   UI live
with Live(layout, refresh_per_second=10, screen=True):
    while running:
        eye = eyes[eye_index]

        layout["cat"].update(Panel(cat(eye)))
        layout["response"].update(Panel(raspuns or "..."))

        eye_index = (eye_index + 1) % len(eyes)

        time.sleep(0.5)