#!Do NOT copy my code!
#!If there is error or issue CONTACT owner! (by discord: ten_siska) or (github: https://github.com/SiskaYT)
#!Do NOT rewrite code under this text it may cause problems (!exept that code where you need to change someting!)!

import psutil
import subprocess
import ctypes
import time

def bl0ck_access_t0_f0lders(f0lder_path):
    FILE_ATTRIBUTE_HIDDEN = 0x02
    FILE_ATTRIBUTE_READONLY = 0x01
    ctypes.windll.kernel32.SetFileAttributesW(f0lder_path, FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_READONLY)

def cl0se_all_expl0rer_windows():
    for pr0cess in psutil.process_iter(['pid', 'name']):
        if pr0cess.info['name'] == 'explorer.exe':
            pr0cess.terminate()

def unbl0ck_access_t0_f0lders(f0lder_path):
    FILE_ATTRIBUTE_NORMAL = 0x80
    ctypes.windll.kernel32.SetFileAttributesW(f0lder_path, FILE_ATTRIBUTE_NORMAL)

def restart_expl0rer():
    subprocess.Popen("explorer.exe")

f0lder_path = "D:/!!duležite!!/Ahoj (nevíš nic)" #Here change the folder what do you want hide if someone will send wrong code

bl0ck_access_t0_f0lders(f0lder_path)
cl0se_all_expl0rer_windows()
time.sleep(300)
unbl0ck_access_t0_f0lders(f0lder_path)
restart_expl0rer()
