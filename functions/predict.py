import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))




def user_context_finder(vectorstore,user_input):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                temperature=0.3)
    retriever = vectorstore.as_retriever()
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Just choose the answers between weather,travelguide,entertainment"
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": user_input})
    return response["answer"]

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