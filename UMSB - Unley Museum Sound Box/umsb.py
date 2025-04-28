# UNLEY MUSEUM SOUNDBOX - UMSB v 1.1
# Tristan Louth-Robins, April 2025
# Adapted from legacy code for Two Sites soundbox (October 2023)

from gpiozero import Button, LED
from time import sleep
import pygame
import datetime as dt
import csv

pygame.mixer.init()

# setup audio files --
audio1 = pygame.mixer.Sound('/home/xyz/Desktop/data/audio1.wav')
audio2 = pygame.mixer.Sound('/home/xyz/Desktop/data/audio2.wav')

# setup leds --
audio1_grn = LED(22)
audio_between = LED(23)
audio2_red = LED(24)

# setup buttons
btn_audio1 = Button(17)  # button to start audio 1 - English audio
btn_audio2 = Button(27)  # button to start audio 2 - Greek audio

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

audio1_channel = pygame.mixer.Channel(0)
audio2_channel = pygame.mixer.Channel(1)

class SiteButton:
    def __init__(self, ledpin, button, filename, audio):
        self.led = ledpin
        self.button = button
        self.file = filename
        self.audio = audio
        self.channel = channel
        self.audio.set_volume(volume_level)
        self.is_playing = False

        print("LED PIN: ", str(self.led))
        print("BUTTON PIN: ", str(self.button))

        self.button.when_pressed = self.handle_press

    def handle_press(self):
        if self.audio.get_num_channels() > 0:
            print(f"{self.file} is currently playing, restarting to avoid overlap...")
            self.audio.stop()
            sleep(0.5)
        else:
            self.channel.stop()
            print(f"{self.file} not playing, all good...")

        pygame.mixer.stop()
        sleep(0.5)
        self.channel.play(self.audio)
        self.is_playing = True
        self.log_interaction()

    def log_interaction(self):
        print("Writing user interaction to dataset.")
        data_write = [str(self.currenttime()), self.file]
        sleep(0.5)
        with open(data_path, 'a', encoding='UTF8', newline='') as data:
            writer = csv.writer(data)
            writer.writerow(data_write)
            print("Data written to csv dataset.\n")

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%d-%m-%Y, %I:%M %p}"

# Instantiate buttons with their logic attached
audio1_action = SiteButton(audio1_grn, btn_audio1, "English dialogue", audio1, audio1_channel)
audio2_action = SiteButton(audio2_red, btn_audio2, "Greek dialogue", audio2, audio2_channel)
