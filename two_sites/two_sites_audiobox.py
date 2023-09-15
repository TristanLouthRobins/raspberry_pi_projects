# TWO SITES (2023) audio player ---
# Version 1.3 (15 SEP 2023) ------
# Tristan Louth-Robins ------------

from gpiozero import Button, LED
from time import sleep
import datetime as dt
import pygame
import csv

# setup leds --
rocky_grn = LED(22)
press_yel = LED(23)
regrw_red = LED(24)

pygame.mixer.init()

# setup audio files --
a_rocky = pygame.mixer.Sound('/home/tristanlouthrobins/Desktop/data/rocky.wav')
a_regrw = pygame.mixer.Sound('/home/tristanlouthrobins/Desktop/data/regrowth.wav')

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

def currenttime():
    now = dt.datetime.now()
    return f"{now:%d-%m-%Y, %I:%M %p}"

def rocky():
    a_regrw.fadeout(2000)
    print("Rocky audio button pressed.")
    press_yel.on()
    sleep(1)
    rocky_grn.on()
    sleep(1)
    a_regrw.set_volume(volume_level)
    pygame.time.delay(100)
    print("################\nplayback started")
    print(a_rocky.get_volume())
    a_rocky.play()
    press_yel.off()
    sleep(4)
    rocky_grn.off()

    print("Writing user interaction to dataset.")

    sleep(1)

    data_write = [str(currenttime()), 'rocky_river', 'Y']

    with open(data_path, 'a', encoding='UTF8', newline='') as data:
        writer = csv.writer(data)
        writer.writerow(data_write)
        # close the csv file 
        print("Data written to csv dataset.\n")
        data.close()


def regrw():
    a_rocky.fadeout(2000)
    print("Regrowth audio button pressed.")
    press_yel.on()
    sleep(1)
    regrw_red.on()
    sleep(1)
    a_regrw.set_volume(volume_level)
    pygame.time.delay(100)
    print("################\nplayback started")
    print(a_rocky.get_volume())
    a_regrw.play()
    press_yel.off()
    sleep(4)
    regrw_red.off()

    print("Writing user interaction to dataset.")

    sleep(1)

    data_write = [str(currenttime()), 'regrowth site', 'Y']

    with open(data_path, 'a', encoding='UTF8', newline='') as data:
        writer = csv.writer(data)
        writer.writerow(data_write)
        # close the csv file 
        print("Data written to csv dataset.\n")
        data.close()

btn_rocky.when_pressed = rocky
btn_regrw.when_pressed = regrw