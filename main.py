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
def processCommand(c):
    print(c)
    pass
    
if __name__ == "__main__":
    speak("Initializing Jarivis....")
    while True:
        # Listen for the wake word 'Jarvis'
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        
        # recognize speech using Google  
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit=1) 
                # listen for the audio input from the microphone 
                # phrase_time_limit is used for the maximum time to listen for a phrase
            word = r.recognize_google(audio)    
            if(word.lower() == "jarvis"):
                speak("Radhe Radhe")
                
                # Listen for the command after the wake word
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand()

        except Exception as e:
            print("Error; {0}".format(e))


