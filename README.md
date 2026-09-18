# 🌐 Translator

A simple and user-friendly web-based language translator built with **Python Flask**.  
The application allows users to translate text between multiple Indian languages, use voice input, and listen to the translated text using text-to-speech.

## 🚀 Features

- 🌐 Text translation
- 🎤 Voice input using the browser microphone
- 🔊 Text-to-speech for translated text
- 📝 Supports user-written text
- 🔄 English to Indian language translation and vice versa
- 📱 Responsive and mobile-friendly interface
- ⚡ Fast and simple Flask backend
- 🛡️ Graceful error handling when online translation services are unavailable
- ❤️ Clean and simple user interface

## 🌍 Supported Languages

| Language | Code |
|----------|------|
| English | `en` |
| Telugu | `te` |
| Hindi | `hi` |
| Tamil | `ta` |
| Kannada | `kn` |
| Marathi | `mr` |

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Web Speech API

### Backend
- Python
- Flask

### APIs / Libraries
- MyMemory Translation API
- Deep Translator
- Google Text-to-Speech (gTTS)
- Requests
- Gunicorn

## 📂 Project Structure

```text
Translator/
│
├── app.py
├── requirements.txt
├── Procfile
├── render.yaml
├── runtime.txt
├── .gitignore
├── .env.example
├── test_cases.md
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css