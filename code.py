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
duration = 1

colorsDark = [0x100000, 0x100500, 0x101000, 0x051000,
0x001000, 0x001005, 0x001010, 0x000010, 0x050010, 0x100005]
colorsLit = [0xFF0000, 0xFFA500, 0xFFFF00, 0xA5FF00,
0x00FF00, 0x00FFA5, 0x00FFFF, 0x0000FF, 0x5500FF, 0xFF00A5]
colorsTarget = [0xFF7700, 0xFFFF00, 0x77FF00, 0x00FF00,
0x00FF77, 0x00FFFF, 0x0077FF, 0x7700FF, 0xFF00FF, 0xFF0077]
tones = [220, 261, 329, 392, 440, 523, 587, 659, 698, 783, 880, 987]

cpx.pixels.brightness = 0.1

def setColor(index):
    for i in range(10):
        cpx.pixels[i] = colorsDark[index]

def startup():
    duration = .5
    red(duration)
    orange(duration)
    yellow(duration)
    yellow2(duration)
    green(duration)
    green2(duration)
    aqua(duration)
    blue(duration)
    indigo(duration)
    violet(duration)
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
    for i in range(10):
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
def yellow2(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[3]
    cpx.play_tone(523, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[3]
def green(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[4]
    cpx.play_tone(587, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[4]
def green2(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[5]
    cpx.play_tone(659, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[5]
def aqua(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[6]
    cpx.play_tone(698, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[6]
def blue(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[7]
    cpx.play_tone(783, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[7]
def indigo(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[8]
    cpx.play_tone(880, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[8]
def violet(duration):
    for i in range(10):
        cpx.pixels[i] = colorsLit[9]
    cpx.play_tone(987, duration)
    for i in range(10):
        cpx.pixels[i] = colorsDark[9]


def getNewTarget(currentLight):
    newTarget = currentLight
    while(newTarget == currentLight or newTarget == 9 or newTarget == 0):
        newTarget = randrange(0, 10)
    return newTarget

steps = 0

while True:
    if stage == "STARTUP":
        if cpx.button_a:
            startup()
            stage = "SETTING TARGET"
    else:
        steps += 1
        if steps % interval == 0:

            if stage == "SETTING TARGET":
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
                        steps = 0
                        target = getNewTarget(currentLight)
                        isIncreasing = False
                        count += 1
                        if count == 5:
                            level += 1
                            count = 0
                            #interval *= 0.9
                            print(f"""level: {level}
count: {count}
interval: {interval}""")
                else:
                    if currentLight == target-1:
                        steps = 0
                        target = getNewTarget(currentLight)
                        isIncreasing = True
                        count += 1
                        if count == 5:
                            level += 1
                            count = 0
                            #interval *= 0.9

