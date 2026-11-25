# Jarvis Voice Assistant

A Python voice assistant inspired by Jarvis from Iron Man. Say the wake word **"Jarvis"**, give a command, and it responds out loud. It can open websites, play songs, read the news, and answer general questions using Google's Gemini API.

> **Status:** Learning project.

## Features

- **Wake word detection:** continuously listens for the word "jarvis" through your microphone.
- **Voice commands:**
  - `open google` opens Google in your browser.
  - `play <song>` opens a song link from your own music library.
  - `news` reads out top US headlines using NewsAPI.
  - Anything else is sent to Gemini, and the answer is spoken back.
- **Speech output:** replies are converted to speech with gTTS and played through pygame.
- **Speech input:** uses the `SpeechRecognition` library with Google's recognizer.

## How it works

```
Microphone → wake word "jarvis" → listen for command → processCommand()
                                                          ├─ open google
                                                          ├─ play <song>   → musicLibrary.py
                                                          ├─ news          → NewsAPI
                                                          └─ anything else → Gemini API
                                                                              ↓
                                                              gTTS → pygame → speaker
```

## Tech stack

- Python 3
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) and PyAudio for microphone input
- [Google Gemini API](https://ai.google.dev/) (`google-genai`) for answering questions
- [gTTS](https://pypi.org/project/gTTS/) and pygame for text-to-speech playback
- [NewsAPI](https://newsapi.org/) for headlines
- python-dotenv for loading API keys

## Getting started

### Prerequisites

- Python 3.11.9
- A working microphone and internet connection
- A [Gemini API key](https://ai.google.dev/) and a [NewsAPI key](https://newsapi.org/)
- Windows is the tested platform (the requirements include Windows-specific packages)

### Installation

```bash
git clone https://github.com/iamvivekmane/jarvis-voice-assistant-python.git
cd jarvis-voice-assistant-python
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key
```

Never commit your `.env` file. Make sure it is listed in `.gitignore`.

### Add your songs

Create `musicLibrary.py` with a dictionary named `music` that maps a one-word song name to a link:

```python
music = {
    "song1": "https://www.youtube.com/watch?v=...",
    "song2": "https://www.youtube.com/watch?v=...",
}
```

Then say "Jarvis", wait for the reply, and say "play song1".

### Run

```bash
python main.py
```

<!-- TODO: replace main.py with your actual script name -->

## Usage

1. Run the script and wait for "Initializing Jarvis".
2. Say **"Jarvis"**. It replies "yaa".
3. Speak your command, for example:
   - "Open Google"
   - "Play song1"
   - "Tell me the news"
   - "What is the capital of France?"

## Project structure

```
jarvis-voice-assistant-python/
├── main.py            # Main loop, wake word, command handling  <!-- TODO: actual filename -->
├── musicLibrary.py    # Song names mapped to links
├── requirements.txt   # Dependencies
├── .env               # API keys (not committed)
└── README.md
```

## Known limitations

- The wake word listener uses very short listening windows, so "jarvis" can be missed or misheard.
- `play` supports only one-word song names.
- Speech recognition and text-to-speech both need an internet connection.
- The news command reads every headline in a row with no way to stop it.
- Errors from Gemini are printed in the terminal but not spoken.

## Ideas for improvement

- Add a dedicated wake-word engine for more reliable activation
- Keep conversation history so Gemini remembers earlier questions
- Add more commands such as weather, reminders, and system controls
- Add a GUI
- Add a "stop" command and limit news to a few headlines

## Author

Vivek Mane
