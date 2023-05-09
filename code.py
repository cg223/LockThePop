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

colorsDark = [0x100000, 0x100500, 0x101000, 0x051000,
0x001000, 0x001005, 0x001010, 0x000010, 0x050010, 0x100005]
colorsLit = [0xFF0000, 0xFFA500, 0xFFFF00, 0xA5FF00,
0x00FF00, 0x00FFA5, 0x00FFFF, 0x0000FF, 0x5500FF, 0xFF00A5]
colorsTarget = [0xFF7700, 0xFFFF00, 0x77FF00, 0x00FF00,
0x00FF77, 0x00FFFF, 0x0077FF, 0x7700FF, 0xFF00FF, 0xFF0077]
tones = [220, 261, 329, 392, 523, 587, 659, 698, 783, 880]

cpx.pixels.brightness = 0.1

def setColor(index):
    for i in range(10):
        cpx.pixels[i] = colorsDark[index]

def startup():
    for i in range(10):
        setColor(i)
        #cpx.play_tone(tones[i], 0.25)
        sleep(0.25)

def getNewTarget(currentLight):
    newTarget = currentLight
    while(newTarget == currentLight or newTarget == 9 or newTarget == 0):
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
                    cpx.pixels[i] = colorsTarget[level]
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
            if isIncreasing:
                if currentLight == target+1:
                    target = getNewTarget(currentLight)
                    isIncreasing = False
                    count += 1
                    if count == 5:
                        level += 1
                        count = 0
                        interval *= 0.9
            else:
                if currentLight == target-1:
                    target = getNewTarget(currentLight)
                    isIncreasing = True
                    count += 1
                    if count == 5:
                        level += 1
                        count = 0
                        interval *= 0.9

