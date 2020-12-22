from music import spotify
from start_project import projects
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

    def process_command(self, text):
        if "song" in text:
            by = None
            position = text.find('by')
            if position > -1:
                by = text[position + 2:].strip()
            spotify.play_music(by)
        if "joke" in text:
            joke = jokes.get_random_joke()
            self.speech(joke)
        if "start a project" in text:
            self.speech("What framework should I start this project on?")
            project_type = self.listen()
            self.speech("What title should I use for this project?")
            title = self.listen()
            projects.start_project(project_type, title)
            change_directory(BASE_DIR)
        if "lights" in text:
            state = text.find('on')
            state = state > -1
            lights.toggle_lights(state)

        with open('logging/transcribed_text.txt', 'a+') as f:
            f.write(text + "\n")

    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Please say something")

            audio = recognizer.listen(source)

            try:
                spoken_text = recognizer.recognize_google(audio).lower()
                self.process_command(spoken_text)
                return spoken_text

            except Exception as e:
                print(f"Error: {str(e)}")

    def speech(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()