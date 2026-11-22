import streamlit as st

st.set_page_config(
    page_title="GenAI Personal Finance Consultant",
    page_icon="💰",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Animated Pink Background */

.stApp {
    background: linear-gradient(
        -45deg,
        #ff9a9e,
        #fad0c4,
        #fbc2eb,
        #a18cd1,
        #ffdde1
    );

    background-size: 400% 400%;
    animation: gradient 12s ease infinite;
}

@keyframes gradient {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Hero Section */

.hero{
    background: rgba(255,255,255,0.30);

    backdrop-filter: blur(18px);

    padding:50px;

    border-radius:25px;

    text-align:center;

    color:#6a0572;

    box-shadow:0 10px 35px rgba(255,105,180,0.35);

    animation: float 4s ease-in-out infinite;
}

@keyframes float{
    0% {transform:translateY(0px);}
    50% {transform:translateY(-10px);}
    100% {transform:translateY(0px);}
}

/* Feature Cards */

.card{
    background: rgba(255,255,255,0.35);

    backdrop-filter: blur(15px);

    border-radius:20px;

    padding:25px;

    color:#4a154b;

    text-align:center;

    transition:0.4s;

    box-shadow:0 8px 25px rgba(255,105,180,0.3);

    min-height:220px;
}

.card:hover{
    transform:translateY(-10px) scale(1.03);
}

/* Statistics Cards */

.stat{
    background: rgba(255,255,255,0.35);

    backdrop-filter: blur(15px);

    border-radius:20px;

    padding:20px;

    color:#6a0572;

    text-align:center;

    box-shadow:0 8px 25px rgba(255,105,180,0.3);
}

/* Footer */

.footer{
    text-align:center;
    color:#4a154b;
    font-size:18px;
    font-weight:bold;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class='hero'>
<h1>💰 GenAI-Powered Personal Finance Consultant</h1>

<h3>
Machine Learning + Generative AI for Personalized Financial Guidance
</h3>

<p>
Analyze UPI Transactions • Predict Risks • Track Goals • Improve Financial Literacy
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# TICKER
# ==========================================

st.markdown("""
<marquee
style="
font-size:20px;
font-weight:bold;
color:#6a0572;
padding:10px;">
💳 UPI Analytics |
📊 Spending Analysis |
⚠️ Risk Prediction |
🎯 Smart Recommendations |
🏆 Goal Planning |
🤖 AI Financial Assistant |
📚 Financial Literacy |
</marquee>
""", unsafe_allow_html=True)

# ==========================================
# STATISTICS
# ==========================================
st.write("")
# ==========================================
# PROJECT MODULES
# ==========================================

st.write("")
st.markdown("## 🚀 Open Project Modules")

# ==========================
# ROW 1
# ==========================

row1 = st.columns(4)

with row1[0]:
    if st.button("📝 Register", use_container_width=True):
        st.switch_page("pages/1_Register.py")

with row1[1]:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/2_Login.py")

with row1[2]:
    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("pages/3_Dashboard.py")

with row1[3]:
    if st.button("💳 UPI Analytics", use_container_width=True):
        st.switch_page("pages/4_UPI_Analytics.py")


# ==========================
# ROW 2
# ==========================

row2 = st.columns(4)

with row2[0]:
    if st.button("🧠 Behavior Analysis", use_container_width=True):
        st.switch_page("pages/5_Behavior_analysis.py")

with row2[1]:
    if st.button("⚠️ Risk Prediction", use_container_width=True):
        st.switch_page("pages/6_Risk_Prediction.py")

with row2[2]:
    if st.button("🎯 Recommendations", use_container_width=True):
        st.switch_page("pages/7_Recommendations.py")

with row2[3]:
    if st.button("🏆 Goal Planning", use_container_width=True):
        st.switch_page("pages/8_Goal_Based_Planning.py")


# ==========================
# ROW 3
# ==========================

row3 = st.columns(4)

with row3[0]:
    if st.button("🔍 Explainable AI", use_container_width=True):
        st.switch_page("pages/9_Explainable_AI.py")

with row3[1]:
    if st.button("💰 Payments", use_container_width=True):
        st.switch_page("pages/10_Payments.py")

with row3[2]:
    if st.button("📚 Financial Literacy", use_container_width=True):
        st.switch_page("pages/11_Financial_Literacy.py")

with row3[3]:
    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/12_Profile.py")


# ==========================
# ROW 4
# ==========================

row4 = st.columns(4)

with row4[0]:
    if st.button("🤖 GenAI Chatbot", use_container_width=True):
        st.switch_page("pages/13_GenAI_Chatbot.py")

with row4[1]:
    if st.button("❤️ Health Score", use_container_width=True):
        st.switch_page("pages/14_Health_Score.py")

with row4[2]:
    if st.button("📊 Experimental Results", use_container_width=True):
        st.switch_page("pages/15_Experimental_Results.py")

with row4[3]:
    if st.button("🎯 Goal Tracker", use_container_width=True):
        st.switch_page("pages/17_Goal_Tracker.py")


# ==========================
# ROW 5
# ==========================

row5 = st.columns(3)

with row5[0]:
    if st.button("🚨 Anomaly Detection", use_container_width=True):
        st.switch_page("pages/anomaly_detection.py")

with row5[1]:
    if st.button("🔮 Spending Prediction", use_container_width=True):
        st.switch_page("pages/prediction.py")

with row5[2]:
    if st.button("💹 Financial Insights", use_container_width=True):
        st.switch_page("pages/16_Financial_Insights.py")
st.markdown("## 📈 Platform Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='stat'>
    <h2>₹12L+</h2>
    <p>Transactions Analyzed</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='stat'>
    <h2>500+</h2>
    <p>Users Assisted</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='stat'>
    <h2>92%</h2>
    <p>Prediction Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='stat'>
    <h2>24/7</h2>
    <p>AI Financial Support</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")


# ==========================================
# FEATURES
# ==========================================

st.markdown("## 🚀 Core Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
    <h1>💳</h1>
    <h3>UPI Analytics</h3>
    <p>
    Analyze transaction history, spending categories and monthly expenses.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h1>📊</h1>
    <h3>User Behavior Analysis</h3>
    <p>
    Discover spending patterns and financial habits using Machine Learning.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <h1>⚠️</h1>
    <h3>Risk Prediction</h3>
    <p>
    Predict overspending risks and budget violations before they occur.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class='card'>
    <h1>🎯</h1>
    <h3>Recommendations</h3>
    <p>
    Personalized suggestions to improve savings and manage expenses.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class='card'>
    <h1>🏆</h1>
    <h3>Goal Planner</h3>
    <p>
    Set and monitor financial goals like education, travel and emergency funds.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class='card'>
    <h1>🤖</h1>
    <h3>GenAI Chatbot</h3>
    <p>
    Ask finance questions and receive intelligent financial guidance instantly.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# RESEARCH CONTRIBUTIONS
# ==========================================

st.markdown("## 🎓 Research Contributions")

st.success("""
✔ UPI Transaction Analytics

✔ User Behavior Analysis

✔ Financial Risk Prediction using Machine Learning

✔ Explainable AI (SHAP)

✔ Personalized Financial Recommendations

✔ Goal-Based Financial Planning

✔ Generative AI Financial Assistant

✔ Financial Literacy Enhancement
""")
