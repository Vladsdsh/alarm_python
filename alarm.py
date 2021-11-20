import time as t
import sys
from playsound import playsound
import emoji

# https://unicode.org/emoji/charts/emoji-list.html


def play_alarm():
    playsound('alarm.mp3', False)
    print('')
    print(emoji.emojize(':speaker_medium_volume:') + emoji.emojize(':speaker_medium_volume:') + emoji.emojize(':speaker_medium_volume:') + emoji.emojize(':speaker_medium_volume:') + emoji.emojize(':speaker_medium_volume:') + emoji.emojize(':speaker_medium_volume:'))
    print(" ---- ALARM --- ")
    t.sleep(10)

def alarm(t_sec):
    print('\033c')
    for i in reversed(range(t_sec)):
        print(emoji.emojize(':alarm_clock:') + " ALARM DANS " + str(i) + " seconds ......")
        t.sleep(1)
        print('\033c')
    play_alarm()

    


alarm(7)
