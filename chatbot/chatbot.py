import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

def get_finance_response(question):

    prompt = f"""
    You are a professional financial consultant.

    Answer the following financial question clearly.

    Question:
    {question}

    Give practical and educational advice.
    """

    response = model.generate_content(prompt)

    return response.text