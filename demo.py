# MicroPython demo - NeoPixel
#Adapted from maxking's repo here https://github.com/maxking/micropython/blob/master/rainbow.py

import time

import machine
import neopixel

pixel_pin = 22
num_pixels = 40

pixels = neopixel.NeoPixel(machine.Pin(pixel_pin), num_pixels)


def wheel(light):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if light < 0 or light > 255:
        return (0, 0, 0)
    if light < 85:
        return (255 - light * 3, light * 3, 0)
    if light < 170:
        light -= 85
        return (0, 255 - light * 3, light * 3)
    light -= 170
    return (light * 3, 0, 255 - light * 3)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.write()
        time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.write()



RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    #pixels.fill(RED)
    #pixels.write()
    # Increase or decrease to change the speed of the solid color change.
    #time.sleep(1)
    #pixels.fill(GREEN)
    #pixels.write()
    #time.sleep(1)
    #pixels.fill(BLUE)
    #pixels.write()
    #time.sleep(1)

    #color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    #color_chase(YELLOW, 0.1)
    #color_chase(GREEN, 0.1)
    #color_chase(CYAN, 0.1)
    #color_chase(BLUE, 0.1)
    #color_chase(PURPLE, 0.1)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
