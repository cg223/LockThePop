from adafruit_circuitplayground.express import cpx
from time import sleep
from random import randrange

isWaiting = False
currrentLight = 0
level = 0
stage = "STARTUP"

colorsDark = [0x220000, 0x221100, 0x222200, 0x112200,
0x002200, 0x002211, 0x002222, 0x000022, 0x110022, 0x220011]
colorsLit = [0xFF0000, 0xFFA500, 0xFFFF00, 0xA5FF00,
0x00FF00, 0x00FFA5, 0x00FFFF, 0x0000FF, 0x5500FF, 0xFF00A5]

cpx.pixels.brightness = 0.1

def setColor(index):
    for i in range(10):
        cpx.pixels[i] = colorsDark[index]

def startup():
    for i in range(10):
        setColor(i)
        sleep(1)

def getTarget():
    pass

while True:
    if stage == "STARTUP":
        startup()
        stage = "PLAYING"
