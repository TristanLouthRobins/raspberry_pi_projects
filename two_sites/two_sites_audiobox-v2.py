# TWO SITES (2023) audio player ---
# Version 1.1 (30 July 2023) ------
# Tristan Louth-Robins ------------

from gpiozero import Button, LED
from time import sleep
import pygame
import datetime as dt

# Initialise pygame mixer
pygame.mixer.init()

class Button:
    def __init__(self, ledpin, button, filename, path):
        self.pin = LED(ledpin)
        self.button = Button(button)
        self.file = filename
        self.path = pygame.mixer.Sound(path)

    def play(self, fadeout, delay, vol_level):
        print(f"{self.file} button pressed.\n")
        print(f"Accessing file from: {self.path}\n")
        print(f"Fadeout is: {fadeout}\n")
        print(f"Delay is: {delay}\n")
        print(f"Volume level: {vol_level}\n")
        ######################################


    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%d-%m-%Y, %I:%M %p}"

rocky = Button(22, 17, "Rocky River", "/Users/tristanlouth-robins/Documents/Documents - MacBook Pro/Python/raspberry_pi_projects/two_sites/data/rocky_river.wav")

print(rocky.play(2000, 2, 0.9))
print(rocky.currenttime())

btn_rocky = rocky.button

btn_rocky.when_pressed = rocky.play(2000, 2, 0.9)