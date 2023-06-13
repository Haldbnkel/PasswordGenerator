import subprocess
import requests
import hashlib
import ctypes
import time
import sys
import os


def refresh():
    try:
        os.remove('./Result.txt')
    except:
        pass

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
        print("Choose Mode!\n[1] Password Generator\n[2] Email Generator\n[3] Combo Generator (Email:Pass)\n[4] 4Letter Generator (xyxy etc)\n")
        mode = input("Mode: ")
        if mode == "1":
            break
        elif mode == "2":
            break
        elif mode == "3":
            break
        elif mode == "4":
            break
    if not mode == "4":
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
    elif mode == "4":
        config = ""
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
        data = input("Generate Mode\nNotype: all\n1: xxxy\n2: xxyy\n3: xyyy\n4: xyxy\n5: xxyx\n6: xyxx\n7: xyyx\n\nExapmle: 134 = xxxy, xyyy, xyxy\n\nMode: ")
        try:
            os.remove('./temp.amoguu')
        except:
            pass
        subprocess.run(args=f"assets.exe -o temp.amoguu -1 {config}{chars} ?1?1")
        message, dupe = "", []
        with open(f"./temp.amoguu", encoding="utf-8") as f:
            lists = f.read().splitlines()
        if data == "":
            data = "1234567"
        for i in lists:
            if i == "":
                continue
            x, y = i[0], i[1]
            if "1" in data:
                if not f"{x}{x}{x}{y}" in dupe:
                    dupe.append(f"{x}{x}{x}{y}")
                    message += f"{x}{x}{x}{y}" + "\n"
            if "2" in data:
                if not f"{x}{x}{y}{y}" in dupe:
                    dupe.append(f"{x}{x}{y}{y}")
                    message += f"{x}{x}{y}{y}" + "\n"
            if "3" in data:
                if not f"{x}{y}{y}{y}" in dupe:
                    dupe.append(f"{x}{y}{y}{y}")
                    message += f"{x}{y}{y}{y}" + "\n"
            if "4" in data:
                if not f"{x}{y}{x}{y}" in dupe:
                    dupe.append(f"{x}{y}{x}{y}")
                    message += f"{x}{y}{x}{y}" + "\n"
            if "5" in data:
                if not f"{x}{x}{y}{x}" in dupe:
                    dupe.append(f"{x}{x}{y}{x}")
                    message += f"{x}{x}{y}{x}" + "\n"
            if "6" in data:
                if not f"{x}{y}{x}{x}" in dupe:
                    dupe.append(f"{x}{y}{x}{x}")
                    message += f"{x}{y}{x}{x}" + "\n"
            if "7" in data:
                if not f"{x}{y}{y}{x}" in dupe:
                    dupe.append(f"{x}{y}{y}{x}")
                    message += f"{x}{y}{y}{x}" + "\n"
            f = open(f'./Result.txt', 'w', encoding="UTF-8")
            f.write(message)
            f.close()
            try:
                os.remove('./temp.amoguu')
            except:
                pass
    print("Complete!")
    time.sleep(3)