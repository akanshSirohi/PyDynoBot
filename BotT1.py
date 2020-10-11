from ctypes import *
from time import sleep
import pyautogui

user= windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
dc = user.GetDC(0)
gdi= windll.LoadLibrary("C:\\Windows\\System32\\gdi32.dll")

def getPixel(x,y):
    rgb = gdi.GetPixel(dc,x,y)
    return (rgb & 0xff,(rgb >> 8) & 0xff,(rgb >> 16) & 0xff)

i=1
x1,y1 = 250,293
x2,y2 = 255,265
while(True):
    avg1 = []
    avg2 = []
    for x in range(x1, x2):
        color1 = getPixel(x, y1)
        color2 = getPixel(x, y2)
        avg1.append(sum(color1)/3)
        avg2.append(sum(color2)/3)
    j=sum(avg1)/(x2-x1)
    d=sum(avg2)/(x2-x1)
    if(j>=40):
        pyautogui.keyDown('space')
        sleep(0.2)
        pyautogui.keyUp('space')
        print("Jump " + str(i))
        i+=1
    elif(d>=40):
        pyautogui.keyDown('down')
        sleep(0.25)
        pyautogui.keyUp('down')
        print("Down " + str(i))
        i += 1

# Dyno Hack Required
# setInterval(()=>{
#     Runner.instance_.currentSpeed=8.5;
#     document.getElementsByTagName('html')[0].className = "offline";
# },100);
