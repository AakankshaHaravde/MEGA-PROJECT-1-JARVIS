import speech_recognition as sr
import webbrowser 
import pyttsx3

# pip install pocketsphinx
# pip install SpeechRecognition
# pip install pyttsx3

recognizer = sr.Recognizer() # is used to recognize speech
engine = pyttsx3.init() # is used to convert text to speech 

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarivis....")
    while True:
        # Listen for the wake word 'Jarvis'
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout = 2) # listen for the audio input from the microphone
            
        print("Recognizing...")
        # recognize speech using Google  

        # recognize speech using Google 
        try:
            command = r.recognize_google(audio)    
            print(command)
            print("Jarvis thinks you said " + r.recognize_sphinx(audio))
        except Exception as e:
            print("Error; {0}".format(e))


