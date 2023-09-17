# TWO SITES (2023) audio player ---
# Version 2.0 dev (17/09/2023) ------
# Tristan Louth-Robins ------------

from gpiozero import Button, LED
from time import sleep
import pygame
import datetime as dt
import csv

pygame.mixer.init()

# setup audio files --
a_rocky = pygame.mixer.Sound('/home/tristanlouthrobins/Desktop/data/rocky.wav')
a_regrw = pygame.mixer.Sound('/home/tristanlouthrobins/Desktop/data/regrowth.wav')

# setup leds --
rocky_grn = LED(22)
press_yel = LED(23)
regrw_red = LED(24)

# setup buttons
btn_rocky = Button(17) # button to start rocky audio
btn_regrw = Button(27) # button to start regrowth audio

volume_level = 0.8 # default volume level

print("Running Two Sites audio playback script\n#####\n")

# ideally the file is only opened when someone presses the button, 
# or the file is written to once enough data is stored in a temp dataframe.
try:
    print("Obtaining the dataset to write interaction data to.\n#####\n")
    # Remember to update path name on RPi
    data_path = '/home/tristanlouthrobins/Desktop/data/two_sites_data.csv'

    # Open in write mode read through the current dataset and print the output
    with open(data_path, encoding='utf-8', newline='') as data:
        # CSV row counter and row reader.
        print("The file has been successfully retrieved.\n#####\n")
        print("# CURRENT TWO SITES DATASET #")
        reader = enumerate(csv.reader(data))
        # Loop through one row at a time, i is counter, row is the entire row
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
        print("LED PIN: ", str(self.led))
        print("BUTTON PIN: ", str(self.button))

    def play(self, fadeout, delay, vol_level):
        print("PLAYBACK STATUS\n#####")
        print(f"{self.file} button pressed.")
        print(f"Fadeout is: {fadeout}")
        print(f"Delay is: {delay}")
        print(f"Volume level: {vol_level}\n")
       
        # Audio ended or switched
        sleep(1)

        print("Writing user interaction to dataset.")

        sleep(1)

        data_write = [str(self.currenttime()), self.file]

        with open(data_path, 'a', encoding='UTF8', newline='') as data:
            writer = csv.writer(data)
            writer.writerow(data_write)
            # close the csv file 
            print("Data written to csv dataset.\n")
            data.close()

        ######################################


    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%d-%m-%Y, %I:%M %p}"

# Instantiate two SiteButton objects for the files
rocky = SiteButton(22, 17, "Rocky River", a_rocky)
regrowth = SiteButton(24, 27, "Regrowth", btn_regrw)

# Actions for when buttons are pressed
btn_rocky.when_pressed = rocky.play(2000, 2, 0.9)
btn_regrw.when_pressed = regrowth.play(2000, 2, 0.9)

#i = 0
#while i < 10:
# print("current count", i)
# i += 1
# print("next count", i)
# sleep(10)

 
# print(rocky.currenttime())

# print(rocky.button)
# btn_rocky.when_pressed = rocky.play(2000, 2, 0.9)