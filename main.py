import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

newsapi = os.getenv('NEWS_API_KEY')
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path, override=True)   
recognizer = sr.Recognizer()
geminiapi = os.getenv('GEMINI_API_KEY')

def speak(text):
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
    elif 'news' in c.lower():
        r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=2b08e2763e5f47ab9c62a234e2576be2')
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
    else:
        prompt = c.lower()
        print('processing with AI')
        client = genai.Client(api_key=geminiapi)
        interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        )
        print(interaction.output_text)
        speak(interaction.output_text)



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
                    print('processing',command)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))



