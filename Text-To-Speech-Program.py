# First you need to install gtts module
# pip install gtts
from gtts import gTTS
import os

f = open('File_Name.txt')
x = f.read()

language = 'en'

audio = gTTS(text=x, lang=language, slow=False)

audio.save('1.wav')  # Audio Format it should be wav
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
