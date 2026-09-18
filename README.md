# SevaVoice — AI Language Translator for Local Services

Hackathon prototype for:

**NN HACKATHON – NIZAMABAD 2026**
**AI LANGUAGE TRANSLATOR FOR LOCAL SERVICES**

## Features

1. Text input
2. Browser voice input
3. Online translation for user-written text
4. Telugu, Hindi, Tamil, Kannada and Marathi output
5. Text-to-speech
6. Hospital / Police / Bank / Government Office phrase library
7. Offline emergency/common-service vocabulary
8. Graceful fallback when the online translator is unavailable
9. Mobile-friendly Bootstrap UI

## Project structure

```text
AI_Language_Translator_Local_Services/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Run on Windows

Open Command Prompt or PowerShell in this folder.

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate it

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
venv\Scripts\activate
```

### 3. Install packages

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

### 5. Open

```text
http://127.0.0.1:5000
```

## Important: internet vs offline

- **Online mode:** used for arbitrary text written by the user.
- **Offline mode:** works only with phrases already stored in `OFFLINE_TRANSLATIONS` in `app.py`.
- Browser voice input and browser text-to-speech depend on browser/device support.

## Hackathon demo

1. Select `Hospital`.
2. Select `English` → `Telugu`.
3. Click `I need a doctor.`.
4. Click `Translate`.
5. Click `Speak Translation`.
6. Demonstrate microphone input.
7. Click `Use Offline Mode`.
8. Disconnect internet and demonstrate an emergency phrase.
9. Explain that offline emergency phrases are intentionally stored locally so basic help remains available during network failure.

## How to extend

Add more languages to `LANGUAGES`.

Add more offline phrases to `OFFLINE_TRANSLATIONS`.

Add service-specific phrases to `SERVICE_PHRASES`.

For a production version, replace the online translator with an approved translation/AI API and add authentication, logging, rate limits and privacy controls.
