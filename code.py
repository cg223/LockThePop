from adafruit_circuitplayground.express import cpx
from time import sleep
from random import randrange

RED = 0xFF0000
GREEN = 0x00FF00
BLUE = 0x0000FF
BLACK = 0x000000
duration = .5

def intro(buns):
    duration = buns
    blue(duration)
    green(duration)
    yellow(duration)
    red(duration)
    duration = .5
    blue(duration)
    red(duration)
    green(duration)
    yellow(duration)
    for i in range(10):
        cpx.pixels[i] = RED
        cpx.play_tone(200, .01)
    sleep(.01)
    for i in range(10):
        cpx.pixels[i] = 0xFFA500
        cpx.play_tone(200, .01)
    sleep(.01)
    for i in range(10):
        cpx.pixels[i] = GREEN
        cpx.play_tone(600, .01)
    cpx.play_tone(800, 1)
    sleep(.01)
    for i in range(10):
        cpx.pixels[i] = BLACK
    sleep(.1)

def red(duration):
    cpx.pixels[3] = RED
    cpx.pixels[4] = RED
    cpx.play_tone(500, duration)
    cpx.pixels[3] = 0x110000
    cpx.pixels[4] = 0x110000

def blue(duration):
    cpx.pixels[0] = BLUE
    cpx.pixels[1] = BLUE
    cpx.play_tone(800, duration)
    cpx.pixels[0] = 0x000011
    cpx.pixels[1] = 0x000011

def yellow(duration):
    cpx.pixels[8] = RED | GREEN
    cpx.pixels[9] = RED | GREEN
    cpx.play_tone(600, duration)
    cpx.pixels[8] = 0x111100
    cpx.pixels[9] = 0x111100

def green(duration):
    cpx.pixels[5] = GREEN
    cpx.pixels[6] = GREEN
    cpx.play_tone(700, duration)
    cpx.pixels[5] = 0x001100
    cpx.pixels[6] = 0x001100

