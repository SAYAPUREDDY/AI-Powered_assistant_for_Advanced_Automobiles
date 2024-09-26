import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS

def create_retrieval_chain():
    loader=CSVLoader(file_path='project/data/Driving_Assistant_Queries_Updated.csv',source_column='Query')
    docs=loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore=FAISS.from_documents(documents=splits, embedding=GoogleGenerativeAIEmbeddings(model = "models/embedding-001"))
    vectorstore.save_local("knowledge_base")
    print("Knowledge base is successfully saved")
    return vectorstore

if __name__=="__main__":
    create_retrieval_chain()
