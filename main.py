import speech_recognition as sr
import webbrowser
import pyttsx3



recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ =='__main__':
    speak('Initializing jarvis...')
    while True:
        # listen all the time for the word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


