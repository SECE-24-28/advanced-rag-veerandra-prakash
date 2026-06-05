from langchain.prompts import PromptTemplate

custom_prompt = PromptTemplate(
    template="""
You are an AI Research Assistant.

Answer ONLY from the provided research paper context.

If the answer is not present in the context,
say:
"I could not find this information in the uploaded research papers."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)