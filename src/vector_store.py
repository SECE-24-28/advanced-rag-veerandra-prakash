from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_db.save_local("faiss_index")

    return vector_db


def load_vector_store():

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )