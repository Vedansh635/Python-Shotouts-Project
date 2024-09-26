# Project-Description

This Python program uses the `pyttsx3` library to provide a text-to-speech conversion functionality. It takes a list of names as input from the user, and then gives a personalized shotout to each name using a male voice.

# How it Works
1. The program initializes the `pyttsx3` engine and sets the voice to male.<br>
2. It sets the speaking rate to 230.<br>
3. The user is prompted to enter a list of names, separated by spaces.<br>
4. The input is split into a list of individual names.<br>
5. The program iterates over each name in the list, saying a personalized shotout message using the `engine.say()` function.<br>
6. The `engine.runAndWait()` function is used to run and wait for the speech to finish before moving on to the next name.<br>

# Features
- Takes multiple names as input from the user<br>
- Provides a personalized shotout to each name using a male voice<br>
- Adjustable speaking rate<br>
- Uses the `pyttsx3` library for text-to-speech conversion<br>

# Requirements
- Python 3.x<br>
- `pyttsx3` library installed<br>

# Usage
1. Run the program in a Python environment.<br>
2. Enter a list of names, separated by spaces, when prompted.<br>
3. The program will give a personalized shotout to each name.<br>
# Feel free to modify it as per your needs!
