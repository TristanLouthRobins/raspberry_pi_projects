# WAV AUDIO PLAYER --------------
# Features volume control -------
# Version 0.1 (24 June 2023) ----
# Tristan Louth-Robins ----------

from gpiozero import Button
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('/home/pi/mu_code/sounds/frogs.wav')
playing = sound.play()

# Button init --------------------
btn_start = Button(17) # button to start playback
btn_stop = Button(27) # button to stop playback
btn_volu = Button(13) # button to raise volume by 0.1
btn_vold = Button(19) # button to lower volume by 0.1
volume_level = 0.5 # default volume level

sound.stop() # initialises playback

def start():
    print("Start button pressed.")
    sound.set_volume(volume_level)
    pygame.time.delay(100)
    print("################\nplayback started")
    print(sound.get_volume())
    sound.play()

def vol_u():
    print("volume up.")
    vol = sound.get_volume()
    if vol < 1:
        vol = vol + 0.1
        sound.set_volume(vol)
        print(sound.get_volume())
    else:
        vol = vol
        print("Max volume reached!")

def vol_d():
    vol = sound.get_volume()
    if vol > 0.1:
        vol = vol - 0.1
        sound.set_volume(vol)
        print(sound.get_volume())
    else:
        vol = vol
        print("Min volume reached!")

def stop():
    print("Stop button pressed.")
    pygame.time.delay(100)
    print("################\nplayback stopped")
    sound.fadeout(2000)
    print("Audio file end.")

btn_start.when_pressed = start
btn_stop.when_pressed = stop
btn_volu.when_pressed = vol_u
btn_vold.when_pressed = vol_d
