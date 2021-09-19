import speech_recognition as sr
from gtts import gTTS
import os
#import pyttsx3

from MyChatBot import MyChatBot

#
# Resources:
#
# https://pypi.org/project/SpeechRecognition/
# https://medium.com/@rahulvaish/speech-to-text-python-77b510f06de
# https://pypi.org/project/pyttsx3/


class MyTextToSpeech:
    
    def __init__(self):
        self.r = sr.Recognizer()
#        self.engine = pyttsx3.init()
#        self.speakup('Hi...')
        self.speak('Hi!')
        self.speech_to_text()
    
    #
    # Uses pyttsx3 Text to Speech API
    #
    def speakup(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()
        
    #
    # Uses Google Text to Speech API
    #
    def speak(self, audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        os.system("afplay audio.mp3")  # mpg321 
    
    #
    # Start listening to user and get reply from BOT
    #
    def speech_to_text(self):
        speech_text = ''
        chatbot = MyChatBot()
        with sr.Microphone() as source:
            
            while speech_text != 'bye':
                print('Listening.....')
                audio = self.r.listen(source, timeout=3)
                print('Looking up....')
                    
                try:
                    speech_text = self.r.recognize_google(audio)            
                    print('Text:', speech_text)
                    reply = chatbot.chatbot_reply(speech_text)
#                    self.speakup(text=reply)
                    self.speak(reply)
                    
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

            
if __name__ == "__main__":
    MyTextToSpeech()
