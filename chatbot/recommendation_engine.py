import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6JHbX6kmS7PoAbOW92P9EApd8b4esIGjf3CT_ybLIooAw")

model = genai.GenerativeModel("models/gemini-2.5-flash")
print(model._model_name)
def generate_ai_recommendations(
        income,
        savings,
        expenses,
        risk,
        behavior,
        top_category):

    prompt = f"""
    Act as an expert financial advisor.

    User Financial Profile:

    Income: ₹{income}
    Savings: ₹{savings}
    Expenses: ₹{expenses}

    Risk Level: {risk}
    Spending Behavior: {behavior}
    Highest Spending Category: {top_category}

    Generate:

    1. Budgeting advice
    2. Savings recommendations
    3. Investment suggestions
    4. Risk reduction tips
    5. Financial literacy tips

    Give personalized recommendations in bullet points.
    """

    response = model.generate_content(prompt)

    return response.text

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

def generate_ai_recommendations(
    income,
    savings,
    expenses,
    risk,
    behavior,
    top_category
):

    prompt = f"""
    You are an expert personal financial advisor.

    User Profile:

    Income: ₹{income}
    Savings: ₹{savings}
    Expenses: ₹{expenses}

    Risk Level: {risk}
    Spending Behavior: {behavior}
    Highest Spending Category: {top_category}

    Generate:

    - Budgeting advice
    - Savings suggestions
    - Investment recommendations
    - Risk reduction tips
    - Financial literacy guidance

    Give personalized recommendations.
    """

    response = model.generate_content(prompt)

    return response.text