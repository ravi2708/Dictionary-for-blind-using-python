from PyDictionary import PyDictionary
from gtts import gTTS
import os
import json
import speech_recognition as sr


def find_meaning(text):
    word = text
    dictionary = PyDictionary(word)
    meaning = dictionary.getMeanings()
    result = json.dumps(meaning)
    print(result)

    file = open("texttospeech.txt","w")
    file.write(result)
    file.close()
    speak()


def speak():
    f=open("texttospeech.txt")
    x = f.read()
    language = "en"
    audio = gTTS(text=x,lang=language,slow=False)
    audio.save("texttospeech.wav")
    os.system("texttospeech.wav")



f=open("introduction.txt")
x = f.read()
language = "en"
audio = gTTS(text=x,lang=language,slow=False)
audio.save("introduction.wav")
os.system("introduction.wav")

r=sr.Recognizer()
print("please talk")
with sr.Microphone() as source:
    audio_data = r.record(source,duration=5)
    print("Recognising...")
    text=r.recognize_google(audio_data)
    find_meaning(text)
