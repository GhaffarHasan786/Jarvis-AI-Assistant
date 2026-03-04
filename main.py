import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

# Text-to-Speech engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speaking

def speak(text):
    """this function use for taking your voice"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """ this function is used to listening your voice """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print(" I'm listening.....Please speak.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language='Eng')
            print(f"you said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            speak("I couldn't hear anything.")
            return ""
        except sr.UnknownValueError:
            speak("I didn't get that,could you repeat it?")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

def execute_command(command):
    """Commands ko execute karta hai"""
    
    if 'youtube' in  command:
        speak("I'm opening Youtube.")
        webbrowser.open('https://www.youtube.com')
    
    elif 'google' in  command:
        speak(" I'm opening Google")
        webbrowser.open('https://www.google.com')
    
    elif 'facebook' in command:
        speak(" I'm opening Facebook")
        webbrowser.open('https://www.facebook.com')
    
    elif 'instagram' in command:
        speak(" I'm opening Instagram")
        webbrowser.open('https://www.instagram.com')
    
    elif 'notepad' in  command:
        speak(" I'm opening Notepad")
        os.system('notepad.exe')
    
    elif 'calculator' in  command:
        speak(" I'm opening Calculator")
        os.system('calc.exe')
    
    elif 'time' in  command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"There still time {current_time}")
    
    elif 'date' in command:
        today = datetime.date.today().strftime("%d %B %Y")
        speak(f"Today Date {today}")
    
    elif 'search' in command:
        speak("What are you searching?")
        search_query = listen()
        if search_query:
            webbrowser.open(f'https://www.google.com/search?q={search_query}')
            speak(f"{search_query} I'm searching for it.")
    
    elif  'stop' in command or 'exit' in command:
        speak("Thanks!")
        return False
    
    else:
        speak("I didn't understand this command.")
    
    return True

def main():
    """Main function - Assistant start karta hai"""
    speak("hi! I'm a assistant for you.")
    speak("Can you open any app for me?")
    
    while True:
        command = listen()
        if command:
            should_continue = execute_command(command)
            if not should_continue:
                break

if __name__ == "__main__":
    main()