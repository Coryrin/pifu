import speech_recognition as sr

def detect_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please say something")

        audio = recognizer.listen(source)

        try:
            spoken_text = recognizer.recognize_google(audio).lower()
            return spoken_text

        except Exception as e:
            print("Error: {}".format(str(e)))

if __name__ == '__main__':
    detect_speech()