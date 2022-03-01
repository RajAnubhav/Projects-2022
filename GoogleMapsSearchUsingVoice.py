# we need to use few modules in python 
'''
List of modules
1. gtts: this will convert the text to speech
2. playsound: this will play the audio
3. speech_recognition: this will convert speech to text
4. webbrowser: this will open the web-browser
'''

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import os

# this is the link of the google-maps
# https://www.google.com/maps/place/

# <<<<<-------------------    asking input from the user    ------------------------>>>>>>>>>>>
def compVoice():
    askText = "Which place you would like to go ?..."
    askAudio= gTTS(text=askText, lang="en-in", slow=False)
    askAudio.save("audio.mp3")
    file= "E:\audio.mp3"
    os.system(file)
    

# <<<<<-------------------    getting the input from the user   ---------------------->>>>>>>>>
def speechSearch():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        userAudio= r.listen(source)
        userText= r.recognize_google(userAudio)
        # now we got the user's input in the text form
        print("Audio successfully received...") 

        return userText

# <<<<<------------------     google searching for the maps     ----------------------->>>>>>>>
def searchForMaps(location):
    webbrowser.open("https://www.google.com/maps/search/"+location)

if __name__=="__main__":
    compVoice()
    mySearch= speechSearch()
    searchForMaps(mySearch)
