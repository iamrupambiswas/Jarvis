import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer and speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
for voice in voices:
    if "male" in voice.name.lower():  # Set to a male voice
        engine.setProperty("voice", voice.id)
        break

# Function to speak the response
def talk(text):
    print(f"Answer: {text}")  # Print the answer
    engine.say(text)
    engine.runAndWait()

# Function to listen for the wake word
def listen_for_wake_word(wake_word="jarvis"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            if wake_word in command:
                return True
        except sr.UnknownValueError:
            pass
    return False

# Function to take a command
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening for command...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print(f"Command: {command}")  # Print the command said
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Please say it again.")
        return ""
    except sr.RequestError as e:
        talk("Sorry, there was an issue with the recognition service.")
        print(f"API Error: {e}")
        return ""
    except Exception as e:
        print(f"Microphone Error: {e}")
        return ""

# Function to process the command
def run_alexa():
    if listen_for_wake_word():
        talk("Hello, how can I assist you, sir?")
        
        while True:
            command = take_command()
            if not command:
                continue  # Skip to the next loop if no command is received
            
            if 'play' in command:
                song = command.replace('play', '').strip()
                print(f"Song name to play: {song}")  # Debugging the song name
                response = f"Playing {song}"
                talk(response)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                response = f"The current time is {time}"
                talk(response)
            elif 'who is' in command:
                person = command.replace('who is', '').strip()
                try:
                    info = wikipedia.summary(person, sentences=1)
                    talk(info)
                except wikipedia.exceptions.DisambiguationError as e:
                    response = f"Too many results for {person}. Please be more specific."
                    talk(response)
                except wikipedia.exceptions.PageError:
                    response = f"Sorry, I couldn't find any information on {person}."
                    talk(response)
            elif 'date' in command:
                response = "Sorry, I have a headache."
                talk(response)
            elif 'are you single' in command:
                response = "I'm in a relationship with WiFi."
                talk(response)
            elif 'joke' in command:
                joke = pyjokes.get_joke()
                talk(joke)
            elif 'stop' in command or 'goodbye' in command:
                talk("Goodbye!")
                break
            else:
                response = "I didn't understand. Can you say that again?"
                talk(response)
    else:
        talk("I didn't hear the wake word, try again.")

# Run the assistant
if __name__ == "__main__":
    try:
        run_alexa()
    except KeyboardInterrupt:
        talk("Goodbye!")
