import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS


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

def weather_answer_chain(weather_report,user_input,city):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                temperature=0.7)
    
    prompt = (f"Here is the current weather information for {city}:\n\n"
              f"{weather_report}\n\n"
              f"Now, the user is asking: '{user_input}'. "
              f"Answer the user's question based on the provided weather data."
              f"be creative and act as a guide to the user."
              f"provide suggestions based on the provided weather data to the user if he asks.")
    response=llm.invoke()