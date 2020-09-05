from gtts import gTTS
import os

def speech(text):
    language = "en"

    voice = gTTS(text=text, lang=language, slow=False)

    voice.save("text.mp3")
    os.system("text.mp3")

if __name__ == '__main__':
    speech("I am called by default")