from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompt import custom_prompt


def build_chain(vector_db):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3
    )

    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={
            "prompt": custom_prompt
        }
    )

    return qa_chain