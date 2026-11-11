import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
recognizer = sr.Recognizer()
# old code
# engine = pyttsx3.init()

def speak(text):
    # old code
    # engine.say(text)
    # engine.runAndWait()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open('https://www.google.com')
    elif c.lower().startswith('play'):
        print('playing a song')
        song = c.lower().split(" ")[1]
        print(song)
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__ =='__main__':
    speak('Initializing jaarvis...')
    r = sr.Recognizer()
    while True:
        # recognize speech using Sphinx
        try:
        # listen all the time for the word jarvis
        # obtain audio from the microphone
            with sr.Microphone() as source:
                print('Listening...')
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=='jarvis'):
                speak('yaa')
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))



