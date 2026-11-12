import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from gtts import gTTS

newsapi = os.getenv('NEWS_API_KEY')
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path, override=True)   
recognizer = sr.Recognizer()
geminiapi = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=geminiapi)
SYSTEM = "You are Jarvis, a voice assistant. Reply in one or two short spoken sentences. No markdown, lists, or emojis."

def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(10)
    pygame.mixer.music.unload()

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
        ask_ai(c)

def ask_ai(prompt):
    try:
        interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=prompt,)
        print(interaction.output_text)
        speak(interaction.output_text)

    except Exception as e:
        print("Gemini error:", e)
        return "Sorry, I couldn't get an answer."

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



