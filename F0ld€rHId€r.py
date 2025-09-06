#!Do NOT copy my code!
#!If there is error or issue CONTACT owner! (by discord: _the_pine_cone_boy_) or (github: https://github.com/SiskaYT)
#!Do NOT rewrite code under this text it may cause problems (!exept that code where you need to change someting!)!

import os
import random
import time

hezl0 = random.randint(10000000, 100000000000000)
place = "C:/Program Files" #Here set place where is your folder saved.
folder = "C:/Program Files/Google Backup" #Folder what do you want open after adding correct code (c0d€.dll) .

time.sleep(5)

with open("c0d€.dll", "w", encoding="utf-8") as file:
    file.write(f"{hezl0}")

time.sleep(10)

with open("c0d€.dll", "w", encoding="utf-8") as file:
    file.write("What are you doing here??!!")

try:
    dáváj = int(input("Davaj:\n"))
    if hezl0 == dáváj:
        os.chdir(place) 
        os.startfile(folder)
    else:
        print("Wrong answer.")
        os.system("python bl0cag€.py")
        os.system(f'attrib +h "{folder}"') #This will hide the folder if someone would say wrong password.
except SyntaxError:
    print("Something went wrong.")
