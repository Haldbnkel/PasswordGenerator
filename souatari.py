import subprocess
import requests
import hashlib
import ctypes
import time
import sys
import os


def refresh():
    f = open(f'./Result.txt', 'w', encoding='UTF-8')
    f.write(f'')
    f.close()

ctypes.windll.kernel32.SetConsoleTitleW(f"Password Generator - Haldbnkel Alpha")

while True:
    try:
        with open('assets.exe', 'rb') as file:
            fileData = file.read()
            hash_md5 = hashlib.md5(fileData).hexdigest()
            break
    except:
        try:
            res = requests.get("https://github.com/Haldbnkel/PasswordGenerator/releases/download/Release/assets.exe", stream=True)
            file_name = os.path.basename("https://github.com/Haldbnkel/PasswordGenerator/releases/download/Release/assets.exe")
            if res.status_code == 200:
                with open('assets.exe', 'wb') as f:
                    f.write(res.content)
        except:
            print("Assets download error. please check internet connection.")
            time.sleep(3)
            sys.exit()

while True:
    if hash_md5 == "5d3793304cb66e5347b78a6888585324":
        break
    try:
        res = requests.get("https://github.com/Haldbnkel/PasswordGenerator/releases/download/Release/assets.exe", stream=True)
        file_name = os.path.basename("https://github.com/Haldbnkel/PasswordGenerator/releases/download/Release/assets.exe")
        if res.status_code == 200:
            with open('assets.exe', 'wb') as f:
                f.write(res.content)
    except:
        print("Assets download error. please check internet connection.")
        time.sleep(3)
        sys.exit()

while True:
    while True:
        os.system('cls')
        print("Password Generator - Haldbnkel Alpha")
        print("Choose Mode!\n[1] Password Generator\n[2] Email Generator\n[3] Combo Generator (Email:Pass)\n")
        mode = input("Mode: ")
        if mode == "1":
            break
        elif mode == "2":
            break
        elif mode == "3":
            break

    os.system('cls')
    print("Format: * = Replace")
    text = input("Text: ")
    config = ""
    if mode == "2" or mode == "3":
        while True:
            twilight = input("Anti Char Mode? (Basically No): ")
            if twilight.lower() == "yes":
                twilight = True
                break
            elif twilight.lower() == "no":
                twilight = False
                break
    else:
        twilight = False
    if mode == "1":
        while True:
            number = input("Big letter? (ABCDE...) [Yes/No]: ")
            if number.lower() == "yes":
                config += "?u"
                break
            elif number.lower() == "no":
                break
        while True:
            number = input("Low letter? (abcde...) [Yes/No]: ")
            if number.lower() == "yes":
                config += "?l"
                break
            elif number.lower() == "no":
                break
        while True:
            number = input("Digits? (1234567890) [Yes/No]: ")
            if number.lower() == "yes":
                config += "?d"
                break
            elif number.lower() == "no":
                break
        chars = input("Chars? (if nothing. press enter.): ")
        letter = text.replace('*', '?1')
        refresh()
        subprocess.run(args=f"assets.exe -o Result.txt -1 {config}{chars} {letter}")
    elif mode == "2":
        while True:
            number = input("letter? [Yes/No]: ")
            if number.lower() == "yes":
                config += "?l"
                break
            elif number.lower() == "no":
                break
        if twilight == True:
            while True:
                number = input("Digits? (1234567890) [Yes/No]: ")
                if number.lower() == "yes":
                    config += "?d"
                    break
                elif number.lower() == "no":
                    break
            chars = input("Chars? (if nothing. press enter.): ")
            letter2 = text.replace('*@', '?2@')
            letter = letter2.replace('*', '?1')
            refresh()
            subprocess.run(args=f"assets.exe -o Result.txt -1 ?l{config}{chars} -2 ?l{config} {letter}")
        else:
            while True:
                number = input("Digits? (1234567890) [Yes/No]: ")
                if number.lower() == "yes":
                    config += "?d"
                    break
                elif number.lower() == "no":
                    break
            chars = input("Chars? (if nothing. press enter.): ")
            letter = text.replace('*', '?1')
            refresh()
            subprocess.run(args=f"assets.exe -o Result.txt -1 {config}{chars} {letter}")
    elif mode == "3":
        while True:
            number = input("letter? [Yes/No]: ")
            if number.lower() == "yes":
                config += "?l"
                break
            elif number.lower() == "no":
                break
        if twilight == True:
            while True:
                number = input("Digits? (1234567890) [Yes/No]: ")
                if number.lower() == "yes":
                    config += "?d"
                    break
                elif number.lower() == "no":
                    break
            chars = input("Chars? (if nothing. press enter.): ")
            letter2 = text.replace('*@', '?2@')
            letter = letter2.replace('*', '?1')
            refresh()
            subprocess.run(args=f"assets.exe -o Result.txt -1 ?l{config}{chars} -2 ?l{config} {letter}:a")
        else:
            while True:
                number = input("Digits? (1234567890) [Yes/No]: ")
                if number.lower() == "yes":
                    config += "?d"
                    break
                elif number.lower() == "no":
                    break
            chars = input("Chars? (if nothing. press enter.): ")
            letter = text.replace('*', '?1')
            refresh()
            subprocess.run(args=f"assets.exe -o Result.txt -1 {config}{chars} {letter}:a")
    print("Complete!")
    time.sleep(3)