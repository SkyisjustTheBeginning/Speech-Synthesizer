from tkinter import *
from gtts import gTTS
from functools import partial
import os
def _Speed_(text):
    text = str(text.get())
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("speech.mp3")
    os.system("speech.mp3")
    return

Bellerophon = Tk()
Bellerophon.title("Bellerophon")
Bellerophon.geometry("200x100")
text = Entry()
text.pack()
_Speed_ = partial(_Speed_, text)
Button(Bellerophon , text = "Convert to speech" , command = _Speed_).pack()
Bellerophon.mainloop()