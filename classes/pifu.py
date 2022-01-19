from inspect import getsourcefile
import os.path
from music import spotify
from light_control import lights
from functions import *
import pyttsx3
import speech_recognition as sr
import jokes
import os

BASE_DIR = os.getcwd()

class Pifu:
    """
        The backbone of the project, Pifu, can listen for & execute commands.
    """
    
    def __init__(self):
        self.listen_to_speech = True

    def handle_play_music(self):
        by = None
        position = self.text.find('by')

        if position > -1:
            by = self.text[position + 2:].strip()

        return spotify.play_music(by)

    def handle_light_change(self):
        room = 1
        if "off" in self.text:
            return lights.toggle_lights(False, room)
        elif "on" in self.text:
            return lights.toggle_lights(True, room)
            
        dim = self.text.find('dim')
        if dim > -1:
            return lights.adjust_brightness(True, room)
        
        return lights.adjust_brightness(False, room)

    def process_command(self):
        if "song" in self.text:
            self.handle_play_music()
        if "joke" in self.text:
            joke = jokes.get_random_joke()
            self.speak(joke)
        if "lights" in self.text:
            self.handle_light_change()
        if "messages" in self.text:
            self.check_messages()

        with open('logging/transcribed_text.txt', 'a+') as f:
            f.write(self.text + "\n")

    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Please say something")

            audio = recognizer.listen(source)

            try:
                spoken_text = recognizer.recognize_google(audio).lower()
                self.text = spoken_text
                self.process_command()

            except Exception as e:
                print(f"Error: {str(e)}")

    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()

    def check_messages(self):
        pass