import csv # this is for importing the CSV files to lists
import random # this is to generate random number
import os # reseting the screen
import time # this lets system wait for a few seconds - delay
from gtts import gTTS 
from os import system

language = 'en'

intro = " Hello, Welcome to TWISTER.  Your hands free game spinner.  Please enter the number of players and time between spins."
spk_intro = gTTS(text=intro, lang=language, slow=False)
spk_intro.save("welcome.mp3")
os.system("start welcome.mp3")
time.sleep(0.5)

N = int(input('How many players? '))
#player1 = input('Player 1's name:')
#player

T = int(input('How much time between spins? (seconds) '))


ready = " Are you ready?"
spk_ready = gTTS(text=ready, lang=language, slow=False)
spk_ready.save("ready.mp3")
os.system("start ready.mp3")


# list of colors and list of limbs (0,1,2,3)
limbs = ["left hand", "right hand", "left foot", "right foot"]
colors = ["red", "yellow", "green", "blue"]

## print random.randint(0,3) # how to do random number

n=1 # start with player 1
#N = int(N)
#T = int(T)

while (1):

    ### THIS PART FOR PLAYER
    speech = "player %s" % (n)
    print("player",n)
    spk_speech = gTTS(text=speech, lang=language, slow=False)
    spk_speech.save("speech.mp3")
    os.system("start speech.mp3")

    if(n<N): # increase to next player, unless max players, then reset to 1
        n=n+1
    else:
        n=1

    ### THIS PART FOR COLOR AND LIMB
    l = limbs[random.randint(0,3)]
    c = colors[random.randint(0,3)]
    print(l,c)
    spin = "%s %s" % (l,c)
    spk_spin = gTTS(text=spin, lang=language, slow=False)
    spk_spin.save("spin.mp3")
    os.system("start spin.mp3")

    time.sleep(T)