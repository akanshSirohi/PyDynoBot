from ctypes import *
from time import sleep
import pyautogui

user= windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
dc = user.GetDC(0)
gdi= windll.LoadLibrary("C:\\Windows\\System32\\gdi32.dll")

def getPixel(x,y):
    rgb = gdi.GetPixel(dc,x,y)
    return rgb

i=1
x1,x2=250,255
y1,y2=293,265
while(True):
    avg1 = []
    avg2 = []
    for x in range(x1, x2):
        color1 = getPixel(x, y1)
        color2 = getPixel(x, y2)
        if(abs(color1-color2)>100):
            pyautogui.keyDown('space')
            sleep(0.1)
            pyautogui.keyUp('space')

# Dyno Hack Required
# setInterval(()=>{
#     Runner.instance_.currentSpeed=8.5;
#     document.getElementsByTagName('html')[0].className = "offline";
# },100);