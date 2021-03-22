import requests
import random
import os
import sys
from colored import fg

color = fg("116")
def start():
    filestart = open("words.txt", "w")
    filestart.write("")
    os.system("title Wordlett - Akiko#4200")
    os.system("cls")
    print(color + """
    
 █     █░ ▒█████   ██▀███  ▓█████▄  ██▓    ▓█████▄▄▄█████▓▄▄▄█████▓
▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒
▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██░    ▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░
░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌▒██░    ▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ 
░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██████▒░▒████▒ ▒██▒ ░   ▒██▒ ░ 
░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░░ ▒░ ░ ▒ ░░     ▒ ░░   
  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ░ ░  ░   ░        ░    
  ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░   ░ ░      ░    ░        ░      
    ░        ░ ░     ░        ░        ░  ░   ░  ░                 
                            ░                                      

    """)


    print(color + "Enter amount of words you wanna generate")
    count = input(">> ")
    maxwords = 26796
    if int(count) > int(maxwords):
        print("Max Words: 26796")
        input("Press ENTER")
        start()

    r = requests.get("https://raw.githubusercontent.com/3wy/Word-26k/main/words.txt")
    rtext = r.text
    print("Please wait while generating...")
    for x in range(int(count)):
        file = open("words.txt", "a")
        file.write(random.choice(rtext.split('\n')) + "\n")
    os.system("cls")
    print("Done Generating, Words saved in words.txt")
    input("Press Enter to close...")
    sys.exit()
start()
