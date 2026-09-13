# 🤖 JARVIS - AI Voice Assistant

A Python-based AI voice assistant inspired by JARVIS.  
It can listen to voice commands, recognize the wake word "Jarvis", open websites, play music, fetch news, answer questions using AI, and respond using AI-generated speech.

## 📌 Project Overview

JARVIS is my **4th Python project**.

The main idea of this project was to build a voice assistant that can:

- Listen to the user's voice
- Detect the wake word "Jarvis"
- Understand voice commands
- Perform predefined tasks
- Fetch information from APIs
- Use AI to answer general questions
- Convert AI responses into speech

This project helped me understand how Python can be integrated with **AI, APIs, speech recognition, text-to-speech, and web automation**.

---

## ✨ Features

- 🎤 Voice Recognition
- 🗣️ Wake Word Detection
- 🤖 AI-Powered Responses
- 🔊 AI Text-to-Speech
- 🌐 Website Opening
- 🎵 Music Playback
- 📰 News Fetching
- 👤 Personalized Commands
- 🔄 Continuous Listening

---

## 🛠️ Technologies Used

| Technology / Library | Purpose |
|---|---|
| Python | Main programming language |
| SpeechRecognition | Converts voice into text |
| ElevenLabs | Converts text into AI-generated speech |
| Groq | Generates AI responses |
| NewsAPI | Fetches news headlines |
| Requests | Sends API requests |
| Webbrowser | Opens websites |
| Music Library | Stores song links |
| Time | Timing-related operations |

---
## 📁 Project Structure
JARVIS-AI-Assistant/
│
├── main.py
│
├── music_library.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── .env
---
## 🔄 Program Flow
                 🚀 START
                    │
                    ▼
          Initialize JARVIS
                    │
                    ▼
        Initialize APIs & Modules
                    │
                    ▼
          Start Microphone
                    │
                    ▼
        Listen for "Jarvis"
                    │
                    ▼
       Is "Jarvis" detected?
              /          \
            No            Yes
            │              │
            │              ▼
            │         "Yes Boss"
            │              │
            │              ▼
            │      Listen for Command
            │              │
            │              ▼
            │      Process Command
            │              │
            │      ┌───────┼────────┐
            │      │       │        │
            │      ▼       ▼        ▼
            │    Website  Music    News
            │      │       │        │
            │      └───────┼────────┘
            │              │
            │              ▼
            │       Unknown Command
            │              │
            │              ▼
            │           Groq AI
            │              │
            │              ▼
            │         AI Response
            │              │
            │              ▼
            │         ElevenLabs
            │              │
            │              ▼
            │        🔊 Voice Output
            │              │
            └──────────────┘
                    │
                    ▼
              Listen Again
---
## 🧩 Command Processing
              🎤 User Voice
                    │
                    ▼
          Speech Recognition
                    │
                    ▼
              Text Command
                    │
                    ▼
          processcommand()
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
    Website       Music         News
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
             Other Command
                    │
                    ▼
                 Groq AI
                    │
                    ▼
              AI Response
                    │
                    ▼
              ElevenLabs
                    │
                    ▼
              🔊 Voice Output
---

## 📦 Python Modules Used

```python
import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import music_library
import requests
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from groq import Groq



