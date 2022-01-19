from music import spotify
from light_control import lights
from functions import *
import pyttsx3
import speech_recognition as sr
import jokes
import requests

class Pifu:
    """
        The backbone of the project, Pifu, can listen for & execute commands.
    """
    
    def __init__(self):
        self.listen_to_speech = True
        self.token = None
        self.tts_engine = pyttsx3.init()

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
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def authenticate_portfolio(self):
        url = 'https://www.corymeikle.com/api/auth/login'
        username = env('PORTFOLIO_EMAIL')
        password = env('PORTFOLIO_PASSWORD')

        r = requests.post(url, data={
            "email": username,
            "password": password
        })

        self.token = r.json()['token']

    def check_messages(self):
        if not self.token:
            self.authenticate_portfolio()

        url = 'https://www.corymeikle.com/api/contact'

        r = requests.get(url, headers={
            'auth-token': self.token
        })

        messages = r.json()

        for i in range(len(messages)):
            message = messages[i]
            name = message['name']
            content = message['content']

            if not message['is_read']:
                self.speak(f'Message from {name}')
                self.speak(content)
