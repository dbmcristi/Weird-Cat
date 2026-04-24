import time
import os
from platform import system
import threading

def cat(eye):
    print("           .'\   /`.")
    print("         .'.-.`-'.-.`.")
    print(f"    ..._:   .-. .-.   :_...")
    print(f"  .'    '-.({eye}) ({eye}).-'    `.")
    print(":  _    _ _`~(_)~`_ _    _  :")
    print(":  /:   ' .-=_   _=-. `   ;\  :")
    print(":   :|-.._  '     `  _..-|:   :")
    print(" :   `:| |`:-:-.-:-:'| |:'   :")
    print(" `.   `.| | | | | | |.'   .'")
    print("    `.   `-:_| | |_:-'   .'")
    print("      `-._   ````    _.-'")
    print("          ``-------''")

eyes = ['o ', ' o']  # stânga-dreapta

# try:
#     while True:
#         for e in eyes:
#             os.system('cls' if os.name == 'nt' else 'clear')  # ștergem doar partea superioară
#             cat(e)
#             # afișăm hello jos
#             # print("\n" * 2 + "hello")  # adaugă linii pentru a poziționa textul mai jos
#             # x = input("la ce te gandesti")
#             # if(x == "nimic"):
#             #     cat('X')
#             #     time.sleep(3)
#             time.sleep(0.6)
# except KeyboardInterrupt:
message = ""  # 🔹 aici ținem HELLO

# def input_thread():
#     global message
#     message = "HELLO"  # se setează o singură dată
#
#
# t = threading.Thread(target=input_thread, daemon=True)
# t.start()

try:
    while True:
        for e in eyes:
            os.system('cls' if os.name == 'nt' else 'clear')
            cat(e)
            print("hi")
            time.sleep(0.6)

except KeyboardInterrupt:
    print("Animație oprită")