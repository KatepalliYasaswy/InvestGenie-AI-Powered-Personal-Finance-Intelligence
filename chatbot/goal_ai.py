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

def generate_goal_strategy(
    goal_name,
    target_amount,
    current_savings,
    monthly_contribution
):

    prompt = f"""
    You are an expert financial planner.

    Goal: {goal_name}

    Target Amount: ₹{target_amount}

    Current Savings: ₹{current_savings}

    Monthly Contribution: ₹{monthly_contribution}

    Generate:

    1. Savings strategy
    2. Budget recommendations
    3. Investment suggestions
    4. Goal achievement tips

    Give concise bullet points.
    """

    response = model.generate_content(prompt)

    return response.text