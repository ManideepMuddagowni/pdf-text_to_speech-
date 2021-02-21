import pyttsx3
import PyPDF2
from gtts import gTTS
import os
from os.path import splitext
mytext = open('ML.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(mytext)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(26, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
