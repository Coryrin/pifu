from music import spotify
from voice_communication import voice_system
from start_project import projects

class Pifu:
    """
        The backbone of the project, Pifu, can listen for & execute commands.

        TODO: Move the logic of main.py into here, making Pifu its own class
    """

    def __init__(self):
        pass

    def process_command(text):
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
        