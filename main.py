import speech_to_txt
import spotify
import voice_system
import jokes

def main():

    text = speech_to_txt.detect_speech()
    print(text)
    
    if "song" in text:
        spotify.play_music()
    elif "joke" in text:
        joke = jokes.get_random_joke()
        voice_system.speech(joke)

    with open('transcribed_text.txt', 'a+') as f:
        f.write(text + "\n")

if __name__ == '__main__':
    main()