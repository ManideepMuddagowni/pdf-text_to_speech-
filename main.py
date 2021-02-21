import pyttsx3
import PyPDF2
from gtts import gTTS
import os
from os.path import splitext
### book name is ML.pdf
mytext = open('ML.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(mytext)
pages = pdfReader.numPages

speaker = pyttsx3.init()
### speech will be starting from 26th page
for num in range(26, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
