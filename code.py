from adafruit_circuitplayground.express import cpx
from time import sleep
from random import randrange

currentLight = 0
level = 0
stage = "STARTUP"
target = 0
isIncreasing = True
count = 0
interval = 0.75

colorsDark = [0x220000, 0x221100, 0x222200, 0x112200,
0x002200, 0x002211, 0x002222, 0x000022, 0x110022, 0x220011]
colorsLit = [0xFF0000, 0xFFA500, 0xFFFF00, 0xA5FF00,
0x00FF00, 0x00FFA5, 0x00FFFF, 0x0000FF, 0x5500FF, 0xFF00A5]
tones = [220, 261, 329, 392, 523, 587, 659, 698, 783, 880]

cpx.pixels.brightness = 0.1

def setColor(index):
    for i in range(10):
        cpx.pixels[i] = colorsDark[index]

def startup():
    for i in range(10):
        setColor(i)
        cpx.play_tone(tones[i], 0.5)
        sleep(0.5)

def getNewTarget(currentLight):
    newTarget = currentLight
    while(newTarget == currentLight):
        newTarget = randrange(0, 10)
    return newTarget

while True:
    if stage == "STARTUP":
        startup()
        stage = "SETTING TARGET"
        
    elif stage == "SETTING LEVEL":
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

        if cpx.button_a:
            if currentLight == target:
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
    sleep(interval)

