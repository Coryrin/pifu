import speech_to_txt
import spotify
import voice_system
import jokes

def main():

    listen = True
    while listen:
        text = speech_to_txt.detect_speech()
        print(text)

        if text is not None:
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

            with open('transcribed_text.txt', 'a+') as f:
                f.write(text + "\n")

if __name__ == '__main__':
    main()