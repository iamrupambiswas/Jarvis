# Voice Assistant

A simple voice assistant built using Python that can perform various tasks like playing YouTube videos, fetching Wikipedia summaries, telling jokes, and providing the current time. The assistant listens for a wake word (default: "jarvis") before executing commands.

## Features
- Speech recognition for voice commands
- Text-to-speech response
- Plays YouTube videos using `pywhatkit`
- Retrieves Wikipedia summaries
- Tells jokes using `pyjokes`
- Fetches the current time
- Wake word detection
- Handles errors gracefully

## Technologies Used
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `wikipedia`
- `pyjokes`
- `datetime`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. Install dependencies:
   ```sh
   pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes
   ```

## Usage

Run the assistant with:
```sh
python voice_assistant.py
```

Say "Jarvis" to activate the assistant, then issue voice commands such as:
- "Play [song name]" → Plays a song on YouTube
- "Who is [person's name]" → Fetches a short Wikipedia summary
- "Tell me a joke" → Tells a joke
- "What time is it?" → Announces the current time
- "Stop" or "Goodbye" → Exits the program

## Example Output
```
Listening for wake word...
Listening for command...
Command: play shape of you
Answer: Playing Shape of You
```

## Contact
- GitHub: [Rupam Biswas](https://github.com/iamrupambiswas)
- LinkedIn: [Rupam Biswas](https://linkedin.com/in/iamrupambiswas)
