import os
import google.generativeai as genai
from functions import weather
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

city = "munich"

weather_report = "schematic diagram of the proposed system"

def conversation():
    while True:
        user_input = "Generate caption"
        if user_input=="Generate caption":

            prompt = (f"Here is the description for the image i have captured\n\n"
                    f"{weather_report}\n\n"
                    f"Now, the user is asking: '{user_input}'. "
                    f"Generate the captin for that image description fo social media "
                    f"Be creative"
                    f"provide three for each in humorous,serious,cute,short and sweet"
                    f"Be precise with the words")

            response = model.generate_content([prompt, weather_report])

            print(f"Assistant: {response.text}")

if __name__
conversation()
