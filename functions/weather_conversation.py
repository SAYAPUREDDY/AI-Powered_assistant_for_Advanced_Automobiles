import speech_recognition as sr
import time
import pyttsx3
import speech_recognition as sr
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from functions import predict
import time
from functions import weather

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
        with sr.Microphone() as source:
            r = sr.Recognizer()
            r.energy_threshold = 1000 
            r.adjust_for_ambient_noise(source, duration=1.2)
            
            while True:
                    try:
                        print("Listening...")
                        audio = r.listen(source)
                        if audio is not None:

                            user_input= r.recognize_google(audio)
                            return user_input
                            
                    except sr.UnknownValueError:
                        print("Sorry, I did not understand that.")
                        speak("Sorry, I did not understand that.")

def weather_bot():
            print("Would you like to know the details of the weather?")
            speak("Would you like to know the details of the weather?")
            time.sleep(2)
            user_input=get_voice_input()
            if "yes" in user_input:
                print("please tell me the location")
                speak("Please tell me the location")
                time.sleep(2)
                location=get_voice_input()
                weather_report=weather.get_weather_updates(location)

                if weather_report:
                        while True:
                            user_input=get_voice_input()
                            print("listening.....")                             
                            response=predict.weather_answer_chain(weather_report,user_input,location)
                            print(response)
                            speak(response)
                            time.sleep(5)
                            if user_input.lower() in ["exit", "quit", "stop"]:
                                print("Assistant: Goodbye! Have a nice day!")
                                break

            elif "no" in user_input:
                    print("Okay , is there anything that i can help u with?")
                    speak("Okay, is there anything that I can help you with?")