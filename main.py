
import pyttsx3
import speech_recognition as sr
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from functions import predict
import time
from functions import weather
from dotenv import load_dotenv

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

    
if __name__ == '__main__':
    print("Welcome to the AI in-car assistant")
    # speak("Welcome to the AI in-car assistant")
    #speak("Welcome to the AI in-car assistant")
    #user_input=get_voice_input()
   

    user_input="is it good day to travel?"
    print(user_input)
    if "exit" in user_input:
        speak("Goodbye")
    else:
        embedding=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        vectorstore = FAISS.load_local("data/knowledge_base", embedding,allow_dangerous_deserialization=True)
        response=predict.user_context_finder(vectorstore,user_input)
        response=response.strip()
        if response == "Weather":
                print("Would you like to know the details of the weather?")
                speak("Would you like to know the details of the weather?")
                # time.sleep(1)
                user_input="yes"
                if "yes" in user_input:
                    print("please tell me the location")
                    speak("Please tell me the location")
                    location="munich"
                    weather_report=weather.get_weather_updates(location)

                    if weather_report:
                         print("Here is the weather report")
                         response=predict.weather_answer_chain(weather_report,location)
                         speak(response)
                elif "no" in user_input:
                     print("Okay , is there anything that i can help u with?")
                     speak("Okay, is there anything that I can help you with?")
                         
