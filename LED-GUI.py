from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

blue = LED(17)
green = LED(27)
red = LED(22)

win=Tk()

win.title("LED GUI")
win.geometry("200x200+800+300")
myFont = tkinter.font.Font(size=18,weight="bold")

def ledToggle():
    clear();
    selectedLedValue =ledValue.get();
    if selectedLedValue ==1:
        blue.on()
    if selectedLedValue ==2:
        green.on()
    if selectedLedValue ==3:
        red.on()
def clear():
    green.off()
    blue.off()
    red.off()
    
    
def exitButton():
    clear()
    win.destroy()
    
 
ledValue =IntVar()
radioBlue = Radiobutton(win, text = 'Blue LED', font=myFont,variable = ledValue , value = 1, command = ledToggle)
radioBlue.pack(anchor = W)
radioGreen = Radiobutton(win, text = 'Green LED', font=myFont,variable = ledValue , value = 2, command = ledToggle)
radioGreen.pack(anchor = W)
radioRed = Radiobutton(win, text = 'Red LED', font=myFont,variable = ledValue , value = 3, command = ledToggle)
radioRed.pack(anchor = W)

eButton = Button(win, text = 'Exit', command = exitButton)
eButton.place(x=140,y=150)

win.mainloop()

