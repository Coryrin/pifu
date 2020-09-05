import speech_to_txt
import spotify

def main():

    text = speech_to_txt.detect_speech()
    print(text)
    
    if "song" in text:
        spotify.play_music()

    with open('transcribed_text.txt', 'a+') as f:
        f.write(text + "\n")

if __name__ == '__main__':
    main()