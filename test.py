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
weather_report = "schematic diagram of the proposed system"

# Conversation loop
def conversation():
    while True:
        # Get user input
        user_input = "Generate caption"

        # If user wants to exit the conversation
        if user_input=="Generate caption":

        # Create prompt based on weather report and user input
            prompt = (f"Here is the description for the image i have captured\n\n"
                    f"{weather_report}\n\n"
                    f"Now, the user is asking: '{user_input}'. "
                    f"Generate the captin for that image description fo social media "
                    f"Be creative"
                    f"provide three for each in humorous,serious,cute,short and sweet"
                    f"Be precise with the words")

            # Generate response from Google Gemini AI model
            response = model.generate_content([prompt, weather_report])

            # Print response from AI
            print(f"Assistant: {response.text}")

if __name__
conversation()
