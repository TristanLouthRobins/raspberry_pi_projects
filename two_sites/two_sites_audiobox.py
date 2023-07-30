# TWO SITES (2023) audio player ---
# Version 1.1 (30 July 2023) ------
# Tristan Louth-Robins ------------

from gpiozero import Button, LED
from time import sleep
import pygame

# setup leds --
rocky_grn = LED(22)
press_yel = LED(23)
regrw_red = LED(24)

# setup audio files --
a_rocky = pygame.mixer.Sound('/home/pi/Desktop/rocky.wav')
a_regrw = pygame.mixer.Sound('/home/pi/Desktop/regrowth.wav')

pygame.mixer.init()
playing = sound.play()

# setup buttons
btn_rocky = Button(17) # button to start rocky audio
btn_regrw = Button(27) # button to start regrowth audio

volume_level = 0.8 # default volume level

sound.stop() # initialises playback

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
    a_rocky.play()
    press_yel.off()
    sleep(4)
    regrw_red.off()

btn_rocky.when_pressed = rocky
btn_regrw.when_pressed = regrw
