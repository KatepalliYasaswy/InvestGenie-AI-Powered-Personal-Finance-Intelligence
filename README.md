# 💎 InvestGenieAI
### Your Personal Finance Intelligence Companion

<p align="center">
  <strong>Track Smarter. Save Better. Plan Your Future.</strong>
</p>

<p align="center">
  An AI-powered personal finance platform that transforms everyday financial transactions into meaningful insights, intelligent recommendations, and better financial decisions.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Generative%20AI-Gemini-4285F4?style=flat-square&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/Explainable%20AI-SHAP-8A2BE2?style=flat-square" />
</p>

---

## ✨ About InvestGenie

Managing money is not just about tracking expenses. It is about understanding spending habits, building savings, identifying financial risks, and making informed decisions for the future.

**InvestGenie** is an AI-powered personal finance intelligence platform designed to make financial management smarter and more accessible.

By combining Machine Learning, Explainable AI, and Generative AI, InvestGenie analyzes UPI-style transactions, identifies spending behaviour, evaluates financial health, detects unusual transactions, and generates personalized financial insights.

From everyday spending analysis to long-term financial goal planning, InvestGenie brings multiple aspects of personal finance into one intelligent platform.

## 💰 Explore Your Financial World

| Financial Module | What It Does |
|:--|:--|
| 💳 UPI Analytics | Understand transactions, income, expenses, and savings |
| 📊 Smart Dashboard | Monitor financial activity and key financial indicators |
| 🧠 Spending Intelligence | Discover spending patterns and behavioural segments |
| ⚠️ Risk Assessment | Evaluate spending-related financial risk |
| 🔍 Anomaly Detection | Identify unusual transactions using Isolation Forest and rule-based checks |
| 💡 AI Recommendations | Receive personalized budgeting and savings suggestions |
| 🎯 Goal Planning | Plan savings for education, travel, vehicles, and other goals |
| 📈 Expense Prediction | Estimate spending using machine learning |
| 💎 Financial Health Score | Evaluate financial wellness using financial indicators |
| 🔬 Explainable AI | Understand the factors influencing model predictions through SHAP |
| 🤖 GenAI Assistant | Explore budgeting, savings, investments, and financial literacy |
| 📄 Financial Reports | Generate downloadable financial summaries |

## 🧠 Intelligence Behind InvestGenie

InvestGenie integrates multiple analytical and AI techniques to understand financial behaviour.

### 01. Spending Behaviour Analysis

**K-Means Clustering**

- Analyzes transaction amounts and spending categories.
- Identifies spending patterns.
- Groups users into behavioural segments.

Behavioural categories include:

- Frugal Saver
- Balanced User
- Impulsive Spender
- Luxury Lifestyle User

### 02. Financial Risk Assessment

**Machine Learning Classification**

- Evaluates income and spending-related indicators.
- Estimates financial risk levels.
- Provides explanations for risk-related results.

### 03. Financial Anomaly Detection

**Isolation Forest**

- Analyzes transaction characteristics.
- Identifies potentially unusual transactions.
- Combines anomaly model outputs with additional rule-based checks.

### 04. Financial Health Intelligence

**Random Forest Regression & Financial Indicators**

- Evaluates income, savings, and expenses.
- Considers savings rate and spending ratio.
- Generates a financial health score.

### 05. Explainable AI

**SHAP – SHapley Additive exPlanations**

- Examines feature contributions.
- Explains model predictions.
- Makes machine learning outputs more interpretable.

### 06. Generative AI

**Google Gemini 2.5 Flash**

- Generates personalized financial insights.
- Provides budgeting and savings suggestions.
- Assists with goal-based financial strategies.
- Answers personal finance and financial literacy questions.

---

## 📊 Financial Intelligence Features

### 💳 Understand Your Money

Explore transaction-level insights and understand where your money goes.

- Income and expense analysis
- Category-wise spending
- Payment-mode analysis
- Transaction summaries

### 🧠 Discover Your Spending Personality

Understand your financial behaviour through clustering and transaction analytics.

### ⚠️ Identify Financial Risks

Analyze spending behaviour and highlight potential financial concerns.

### 💡 Get Personalized Financial Insights

Receive suggestions based on income, expenses, savings, spending behaviour, and financial risk.

### 🎯 Turn Goals into Action Plans

Plan for:
- Education
- Travel
- Emergency funds
- Car purchases
- Home purchases
- Retirement

Calculate remaining savings, monthly contributions, goal progress, and estimated completion time.

### 🤖 Talk to Your Financial Assistant

Explore topics such as:
- Budgeting
- Savings strategies
- Investment concepts
- UPI spending
- Financial planning
- Financial literacy

---

## 🛠️ Technology Stack

| Category | Technologies |
|:--|:--|
| Programming | Python |
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Clustering | K-Means |
| Anomaly Detection | Isolation Forest |
| Prediction | Random Forest, Linear Regression |
| Explainable AI | SHAP |
| Generative AI | Google Gemini API |
| Visualization | Plotly |
| Database | SQLite |
| Model Persistence | Joblib, Pickle |
| Report Generation | ReportLab |
| Payment Integration | Razorpay Checkout |

---

## 🔄 How InvestGenie Works

```text
             USER ACCESS
                  |
                  v
        FINANCIAL TRANSACTION DATA
                  |
                  v
           DATA PROCESSING
                  |
                  v
        FINANCIAL DATA ANALYTICS
                  |
        +---------+---------+
        |         |         |
        v         v         v
     SPENDING   FINANCIAL  ANOMALY
     ANALYSIS    HEALTH   DETECTION
        |         |         |
        v         v         v
      K-MEANS   HEALTH     ISOLATION
     CLUSTERING  SCORING    FOREST
        |         |         |
        +---------+---------+
                  |
                  v
          FINANCIAL INSIGHTS
                  |
          +-------+-------+
          |       |       |
          v       v       v
        RISK    EXPLAIN-  GENAI
      ANALYSIS   ABILITY  ASSISTANT
          |       |       |
          +-------+-------+
                  |
                  v
        PERSONALIZED GUIDANCE
                  |
          +-------+-------+
          |       |       |
          v       v       v
        SAVING   GOAL    FINANCIAL
        PLANS   TRACKING  REPORTS
                  |
                  v
         FINANCIAL DASHBOARD
```

## 📁 Project Architecture

```text
InvestGenie/
│
├── Home.py
├── requirements.txt
│
├── chatbot/
│   ├── chatbot.py
│   ├── goal_ai.py
│   └── recommendation_engine.py
│
├── components/
│   └── chatbot_widget.py
│
├── data/
│   └── transactions.csv
│
├── ml/
│   ├── behavior_clustering.py
│   ├── financial_health_score.py
│   ├── risk_prediction.py
│   ├── train_risk_model.py
│   ├── user_behavior.py
│   └── xai_explainer.py
│
├── models/
│   ├── risk_model.pkl
│   ├── spending_model.pkl
│   ├── anomaly_model.pkl
│   └── encoders/
│
├── pages/
│   ├── 1_Register.py
│   ├── 2_Login.py
│   ├── 3_Dashboard.py
│   ├── 4_UPI_Analytics.py
│   ├── 5_Behavior_analysis.py
│   ├── 6_Risk_Prediction.py
│   ├── 7_Recommendations.py
│   ├── 8_Goal_Based_Planning.py
│   ├── 9_Explainable_AI.py
│   ├── 10_Payments.py
│   ├── 11_Financial_Literacy.py
│   ├── 13_GenAI_Chatbot.py
│   ├── 14_Health Score.py
│   ├── 18_Financial_Insights.py
│   └── 19_Goal_Tracker.py
│
└── utils/
    ├── behavior_clustering.py
    ├── charts.py
    ├── db.py
    ├── expense_forecast.py
    ├── recommendation_engine.py
    ├── report_generator.py
    └── xai_explainer.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/your-username/InvestGenie.git
```

### 2. Navigate to the project directory

```bash
cd InvestGenie
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install streamlit pandas numpy plotly scikit-learn shap joblib google-generativeai python-dotenv reportlab python-dateutil
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Keep API keys private. Never commit your `.env` file to GitHub.

### 6. Launch InvestGenie

```bash
streamlit run Home.py
```

Open the local URL displayed in your terminal.

---

## 🔐 Security & Responsible Finance

- Keep API credentials in environment variables.
- Avoid uploading real personal financial information.
- Use anonymized or synthetic transaction data for demonstrations.
- Secure authentication credentials with password hashing.
- Treat AI-generated recommendations as informational guidance.
- Verify payment integration and transaction handling before production deployment.

## 🔮 Future Enhancements

- Real-time transaction analytics through authorized financial data integrations.
- Advanced spending and cash-flow forecasting.
- Improved financial anomaly detection.
- Interactive investment portfolio tracking.
- Advanced savings optimization.
- Mobile-friendly financial dashboard.
- More comprehensive model evaluation and explainability.

## ⚠️ Disclaimer

InvestGenie is an educational personal finance analytics project. Its predictions, financial scores, and AI-generated suggestions are intended for informational purposes only. They are not guaranteed financial outcomes or professional investment advice.

## 👩‍💻 Skills & Concepts Demonstrated

`Python` · `Financial Analytics` · `UPI Transaction Analysis` · `Machine Learning` · `K-Means Clustering` · `Random Forest` · `Anomaly Detection` · `Explainable AI` · `SHAP` · `Generative AI` · `Google Gemini` · `Streamlit` · `Data Visualization` · `SQLite`

---

<p align="center">
  <strong>💎 INVESTGENIE</strong>
</p>

<p align="center">
  <em>Understand Your Money. Empower Your Future.</em>
</p>

<p align="center">
  Built with Python, Machine Learning & Generative AI.
</p>

<p align="center">
  ⭐ If you like this project, consider giving it a star!
</p>
