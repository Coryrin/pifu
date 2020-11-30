import pyttsx3

def speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    speech("Hello World")