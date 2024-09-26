import os
import google.generativeai as genai
from functions import weather
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the city for weather report
city = "munich"

# Get weather information for the city
weather_report = weather.get_weather_updates(city)

# Conversation loop
def conversation():
    while True:
        # Get user input
        user_input = input("User: ")

        # If user wants to exit the conversation
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("Assistant: Goodbye! Have a nice day!")
            break

        # Create prompt based on weather report and user input
        prompt = (f"Here is the current weather information for {city}:\n\n"
                  f"{weather_report}\n\n"
                  f"Now, the user is asking: '{user_input}'. "
                  f"Answer the user's question based on the provided weather data. "
                  f"Be creative and act as a guide to the user. "
                  f"Provide suggestions based on the provided weather data if user asks as suggest me."
                  f"Be precise with the words and only reply to the question")

        # Generate response from Google Gemini AI model
        response = model.generate_content([prompt, weather_report])

        # Print response from AI
        print(f"Assistant: {response.text}")


