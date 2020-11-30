import speech_to_txt
import jokes
import os
from music import spotify
from voice_communication import voice_system
from start_project import projects
from light_control import lights

BASE_DIR = os.getcwd()
def main():

    listen = True
    while listen:
        text = speech_to_txt.detect_speech()

        if text is not None:
            print(text)
            if "song" in text:
                by = None
                position = text.find('by')
                if position > -1:
                    by = text[position + 2:].strip()
                spotify.play_music(by)
            if "joke" in text:
                joke = jokes.get_random_joke()
                voice_system.speech(joke)
            if text == "quit":
                listen = False
            if "start a project" in text:
                voice_system.speech("What framework should I start this project on?")
                project_type = speech_to_txt.detect_speech()
                voice_system.speech("What title should I use for this project?")
                title = speech_to_txt.detect_speech()
                projects.start_project(project_type, title)
                reset_directory()
            if "lights" in text:
                state = text.find('on')
                state = state > -1
                lights.toggle_lights(state)

            with open('voice_communication/transcribed_text.txt', 'a+') as f:
                f.write(text + "\n")

def reset_directory():
    os.chdir(BASE_DIR)


if __name__ == '__main__':
    main()