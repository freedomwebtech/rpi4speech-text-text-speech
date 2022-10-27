import speech_recognition as sr
import wikipedia
from gtts import gTTS
import os
from datetime import datetime

now = datetime.now()  

def speak(b):
    tts = gTTS(text=b, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")



def speech_to_text():

    required=-1
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required= index
    r = sr.Recognizer()
    with sr.Microphone(device_index=required) as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=4)
    try:
        input = r.recognize_google(audio)
#        print("You said: " + input)
        return str(input)
       
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
while True:        
     a=str(speech_to_text())        
     print(a)
     if a=='None':
         print(" ")
    
    
     elif a=="what is today":
         k=now.strftime("Today is %A %d/%m/%y" )
         print(k)
         speak(k)
     elif a=="time now":
         k1=now.strftime("it's %-I:%-M %P")
         print(k1)
         speak(k1)
     else:    
         result = wikipedia.summary(a, sentences = 2) 
         print(result)
         speak(result)