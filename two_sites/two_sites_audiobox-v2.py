# TWO SITES (2023) audio player ---
# Version 2.0 dev (8 Sep 2023) ------
# Tristan Louth-Robins ------------

# from gpiozero import Button, LED
from time import sleep
import pygame
import datetime as dt

# Initialise pygame mixer
pygame.mixer.init()

print("Running Two Sites audio playback script\n#####\n")

# ideally the file is only opened when someone presses the button, 
# or the file is written to once enough data is stored in a temp dataframe.
try:
    print("Obtaining the dataset to write interaction data to.\n#####\n")
    data = open('/Users/tristanlouth-robins/Documents/Documents - MacBook Pro/Python/raspberry_pi_projects/two_sites/data/two_sites_data.csv')
    print("The file has been successfully retrieved.\n#####\n")
except FileNotFoundError:
    print("THE SPECIFIED FILE COULD NOT BE FOUND.")
except Exception:
    print("Something else went wrong here.")

class But:
    def __init__(self, ledpin, button, filename, path):
        self.pin = ledpin
        self.button = button
        self.file = filename
        self.path = pygame.mixer.Sound(path)

    def play(self, fadeout, delay, vol_level):
        print("PLAYBACK STATUS\n#####")
        print(f"{self.file} button pressed.")
        print(f"Accessing file from: {self.path}")
        print(f"Fadeout is: {fadeout}")
        print(f"Delay is: {delay}")
        print(f"Volume level: {vol_level}")
        ######################################


    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%d-%m-%Y, %I:%M %p}"

rocky = But(22, 17, "Rocky River", '/Users/tristanlouth-robins/Documents/Documents - MacBook Pro/Python/raspberry_pi_projects/two_sites/data/rocky_river.wav')

print(rocky.play(2000, 2, 0.9))
print(rocky.currenttime())

print(rocky.button)

# btn_rocky.when_pressed = rocky.play(2000, 2, 0.9)