from playsound import playsound
import time

CLEAR = "\033[2J" # ANSII code for clearing screen
CLEAR_AND_RETURN = "\033[H" # ANSII code for clearing screen and returning everytime
def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left//3600
        minutes_left = (time_left%3600)//60
        seconds_left = (time_left%3600)%60
        print(f"{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
    playsound("Alarm1.mp3")

hours = int(input("How many hourss to wait:"))
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = hours*3600 + minutes*60 + seconds
alarm(total_seconds)