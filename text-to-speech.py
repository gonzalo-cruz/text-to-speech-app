from gtts import gTTS 
import os
from tkinter import *

root = Tk()
root.title("Text to speech converter")
l = Label(root, text = "Insert text to be read")
l.config(font =("Consolas bold", 30), pady = 70)
l.pack()
canvas = Canvas(root, width=400, height = 300)
canvas.pack()

def tts():
    text = entry.get()
    output = gTTS(text=text,lang='es',slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")

entry = Entry(root)
canvas.create_window(200,70,window=entry)

button = Button(text="Go",command = tts)
canvas.create_window(200,100,window = button)

root.mainloop()