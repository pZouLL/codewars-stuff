from datetime import datetime
import time
import os

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print(current_time)
until_when_h = int(input("How Many Hours : "))
until_when_m = int(input("How Many Minutes : "))
until_when_s = int(input("How Many  Seconds: "))

untilS = until_when_h * 3600
untilM = until_when_m * 60

seconds = untilS + untilM + until_when_s

loop = 1
while loop == 1 :
    time.sleep(1)
    seconds -= 1 
    if seconds == 0 :
        print("Countdown Done")
        loop = 2

import winsound

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)