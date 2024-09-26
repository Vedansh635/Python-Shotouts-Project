# This program will take input of multiple names and then give a shotout to all of them using `pyttsx3` library
# `pyttsx3` is a text-to-speech conversion library in Python.

import pyttsx3

# initializing the engine
engine = pyttsx3.init()

# getting the list of available voices
voices = engine.getProperty('voices')

# setting the voice to male (0 for male, 1 for female)
engine.setProperty('voice',voices[0].id)

# getting the current speaking rate
rate = engine.getProperty('rate')

# setting the new speaking rate
engine.setProperty('rate', 230)

# taking input of names from user
names = input('Enter names and enter space to add new names: ')

# splitting the input into a list of names
names_list = names.split()

# iterating over each name in the list
for name in names_list:
    # saying the shotout for each name
    engine.say(f'Shotout to {name}')
    # running and waiting for the speech to finish
    engine.runAndWait()
