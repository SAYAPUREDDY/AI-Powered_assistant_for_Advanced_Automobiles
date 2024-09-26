import google.generativeai as genai
def weather_answer_chain(weather_report,city):
        model = genai.GenerativeModel("gemini-1.5-flash")
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
            return(f"Assistant: {response.text}")