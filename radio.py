# TTS Radio
# © 2020 Aconix All Rights Reserved

import config
import win32com.client as wincl
import winsound
import time
import os
import random

speak = wincl.Dispatch("SAPI.SpVoice")

files = os.listdir("sounds")
file_count = len(files)

print(r"""
 /$$$$$$$$ /$$$$$$$$ /$$$$$$        /$$$$$$$                  /$$ /$$          
|__  $$__/|__  $$__//$$__  $$      | $$__  $$                | $$|__/          
   | $$      | $$  | $$  \__/      | $$  \ $$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$ 
   | $$      | $$  |  $$$$$$       | $$$$$$$/ |____  $$ /$$__  $$| $$ /$$__  $$
   | $$      | $$   \____  $$      | $$__  $$  /$$$$$$$| $$  | $$| $$| $$  \ $$
   | $$      | $$   /$$  \ $$      | $$  \ $$ /$$__  $$| $$  | $$| $$| $$  | $$
   | $$      | $$  |  $$$$$$/      | $$  | $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/
   |__/      |__/   \______/       |__/  |__/ \_______/ \_______/|__/ \______/ 

© 2020 Aconix All Rights Reserved
    """)


time.sleep(2)
print("REFER TO THE README FOR HELP")
print()
time.sleep(2)
print("The sounds folder contains " + str(file_count) + " song(s)")

i = 0

while i <= 10:
    music = random.choice(files)
    musicNoExt = os.path.splitext(music)[0]
    speak.Speak(config.upNext1 + musicNoExt + config.upNext2)
    speak.Speak(config.announcement)
    print ("Now Playing: " + musicNoExt)
    winsound.PlaySound("sounds/" + music, winsound.SND_ALIAS)
    print(config.idleMessage)
    speak.Speak(config.justPlayed1 + musicNoExt + config.justPlayed2)