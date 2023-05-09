from adafruit_circuitplayground.express import cpx
from time import sleep
from random import randrange

currentLight = 0
level = 0
stage = "STARTUP"
target = 0
isIncreasing = True
count = 0
interval = 5000
duration = .5

colorsDark = [0x110000, 0x110800, 0x111100, 0x081100,
0x001100, 0x001108, 0x001111, 0x000011, 0x080011, 0x110008]
colorsLit = [0xFF0000, 0xFFA500, 0xFFFF00, 0xA5FF00,
0x00FF00, 0x00FFA5, 0x00FFFF, 0x0000FF, 0x5500FF, 0xFF00A5]
tones = [200, 220, 261, 300, 329, 350, 392, 400, 450, 500, 523, 550 587, 600, 659, 650, 698, 700, 750, 783, 880, 800]

cpx.pixels.brightness = 0.1

def setColor(index):
    for i in range(10):
        cpx.pixels[i] = colorsDark[index]

def startup():
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
        cpx.pixels[i] = colorsLit[0]
        cpx.play_tone(200, .01)
    sleep(.01)
    for i in range(10):
        cpx.pixels[i] = 0xFFA500
        cpx.play_tone(200, .01)
    sleep(.01)
    for i in range(10):
        cpx.pixels[i] = colorsLit[4]
        cpx.play_tone(600, .01)
    cpx.play_tone(800, 1)
    sleep(.01)
    for i in range(10):
        cpx.pixels[i] = 0x000000
    sleep(.1)

def red(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[0]
    cpx.play_tone(329, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[0]
def orange(duration):
    for in range(10)
        cpx.pixels[i] = colorsLit[1]
    cpx.play_tone(392, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[1]
def yellow(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[2]
    cpx.play_tone(440, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[2]


def getNewTarget(currentLight):
    newTarget = currentLight
    while(newTarget == currentLight):
        newTarget = randrange(0, 10)
    return newTarget

steps = 0

while True:
    steps += 1
    if steps % interval == 0:
        if stage == "STARTUP":
            startup()
            stage = "SETTING TARGET"

        elif stage == "SETTING TARGET":
            target = getNewTarget(currentLight)
            stage = "PLAYING"

        elif stage == "PLAYING":
            for i in range(10):
                if i == target:
                    cpx.pixels[i] = colorsLit[level-1]
                elif i == currentLight:
                    cpx.pixels[i] = colorsLit[level]
                else:
                    cpx.pixels[i] = colorsDark[level]

            if isIncreasing:
                currentLight += 1
            else:
                currentLight -= 1

            if currentLight == -1:
                currentLight = 9
            elif currentLight == 10:
                currentLight = 0

    if stage == "PLAYING":
        if cpx.button_a:
            print('a_button')
            if currentLight == target:
                print('correct')
                stage = "SETTING LEVEL"
                if isIncreasing:
                    isIncreasing = False
                else:
                    isIncrease = True

                count += 1
                if count == 5:
                    level += 1
                    count = 0
                    interval *= 0.9
            else:
                continue
            print()

