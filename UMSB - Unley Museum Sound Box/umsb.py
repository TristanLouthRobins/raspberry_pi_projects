# UNLEY MUSEUM SOUNDBOX - UMSB v.1
# Tristan Louth-Robins, April 2025
# Adapted from legacy code for Two Sites soundbox (October 2023)

from gpiozero import Button, LED
from time import sleep
import pygame
import datetime as dt
import csv

pygame.mixer.init()

# setup audio files --
a_rocky = pygame.mixer.Sound('/home/tristanlouthrobins/Desktop/data/audio1-eng.wav')
a_regrw = pygame.mixer.Sound('/home/tristanlouthrobins/Desktop/data/audio2-gre.wav')

# setup leds --
rocky_grn = LED(22)
press_yel = LED(23)
regrw_red = LED(24)

# setup buttons
btn_rocky = Button(17)  # button to start audio 1 - English audio
btn_regrw = Button(27)  # button to start audio 2 - Greek audio

volume_level = 0.8  # default volume level

print("Running UMSB audio playback script\n#####\n")

try:
    print("Obtaining the dataset to write interaction data to.\n#####\n")
    data_path = '/home/tristanlouthrobins/Desktop/data/unley_museum_data_2025.csv'

    with open(data_path, encoding='utf-8', newline='') as data:
        print("The file has been successfully retrieved.\n#####\n")
        print("# CURRENT UNLEY MUSEUM DATASET #")
        reader = enumerate(csv.reader(data))
        for i, row in reader:
            print(i, row)
    print("Read complete.\n")
except FileNotFoundError:
    print("THE SPECIFIED FILE COULD NOT BE FOUND.")
except Exception:
    print("Something else went wrong here.")

class SiteButton:
    def __init__(self, ledpin, button, filename, audio):
        self.led = ledpin
        self.button = button
        self.file = filename
        self.audio = audio
        self.audio.set_volume(volume_level)
        self.is_playing = False

        print("LED PIN: ", str(self.led))
        print("BUTTON PIN: ", str(self.button))

        self.button.when_pressed = self.handle_press

    def handle_press(self):
        if self.audio.get_num_channels() > 0:
            print(f"{self.file} is currently playing, restarting...")
            self.audio.stop()
            sleep(0.5)
        else:
            print(f"{self.file} not playing, starting over...")

        self.audio.play()
        self.is_playing = True
        self.log_interaction()

    def log_interaction(self):
        print("Writing user interaction to dataset.")
        data_write = [str(self.currenttime()), self.file]
        with open(data_path, 'a', encoding='UTF8', newline='') as data:
            writer = csv.writer(data)
            writer.writerow(data_write)
            print("Data written to csv dataset.\n")

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%d-%m-%Y, %I:%M %p}"

# Instantiate buttons with their logic attached
rocky = SiteButton(rocky_grn, btn_rocky, "English", a_rocky)
regrowth = SiteButton(regrw_red, btn_regrw, "Greek", a_regrw)