import csv # this is for importing the CSV files to lists
import random # this is to generate random number
import os # reseting the screen
import time # this lets system wait for a few seconds - delay
import itertools
from gtts import gTTS 

from os import system

#os.system('clear')
language = 'en'
intro = " Hello, Welcome to TWISTER.  Your hands free game spinner.  Please enter the number of players and time between spins."
spk_intro = gTTS(text=intro, lang=language, slow=False)
spk_intro.save("welcome.mp3")
os.system("start welcome.mp3")
time.sleep(0.5)

player_names = []

input_players = int(input('Number of Players:'))

for i in range(0,input_players):
  name = input('Enter player name: ')
  player_names.append(name)

T = int(input('How much time between spins? (seconds) '))


ready = " Are you ready?"
spk_ready = gTTS(text=ready, lang=language, slow=False)
spk_ready.save("ready.mp3")
os.system("start ready.mp3")

# list of colors and list of limbs (0,1,2,3)
limbs = ["left hand", "right hand", "left foot", "right foot"]
colors = ["red", "yellow", "green", "blue"]

#while (1):

    ### THIS PART FOR PLAYER
for element in itertools.cycle(player_names):
    speech = element
    print(element)
    spk_speech = gTTS(text=speech, lang=language, slow=False)
    spk_speech.save("speech.mp3")
    os.system("start speech.mp3")


    ### THIS PART FOR COLOR AND LIMB
    l = limbs[random.randint(0,3)]
    c = colors[random.randint(0,3)]
    print(l,c)
    spin = "%s %s" % (l,c)
    spk_spin = gTTS(text=spin, lang=language, slow=False)
    spk_spin.save("spin.mp3")
    os.system("start spin.mp3")

    time.sleep(T)
    