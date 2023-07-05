# pip install gtts
from gtts import gTTS
# pip install os
import os

mytext = 'Your Text :)'

language = 'en'

myobj = gTTS(text = mytext, lang = language, slow = False)

myobj.save("file_name.mp3")
os.system("mp3 file_name.mp3")
