import streamlit as st
import streamlit.components.v1 as components
import razorpay
import os
from dotenv import load_dotenv

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Premium Subscription",
    page_icon="💎",
    layout="centered"
)

# ==========================
# LOAD ENV VARIABLES
# ==========================
load_dotenv()

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")

if not RAZORPAY_KEY_ID or not RAZORPAY_SECRET:
    st.error("Razorpay credentials not found in .env file")
    st.stop()

# ==========================
# RAZORPAY CLIENT
# ==========================
client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET)
)

# ==========================
# UI
# ==========================
st.title("💎 Premium Subscription")

st.markdown("""
### Unlock Premium Features

✅ Unlimited Predictions

✅ AI Assistant Access

✅ Advanced Analytics

✅ Download Reports

✅ Priority Support

---

### Price: ₹499
""")

# ==========================
# CREATE ORDER
# ==========================
try:
    order = client.order.create({
        "amount": 49900,  # ₹499 in paise
        "currency": "INR",
        "payment_capture": 1
    })

except Exception as e:
    st.error(f"Order Creation Failed: {e}")
    st.stop()

# ==========================
# PAYMENT BUTTON
# ==========================
payment_html = f"""
<!DOCTYPE html>
<html>
<head>
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
</head>

<body>

<button id="pay-btn"
style="
background:#3399cc;
color:white;
border:none;
padding:12px 25px;
font-size:18px;
border-radius:8px;
cursor:pointer;
">
🚀 Pay ₹499
</button>

<script>

var options = {{

    "key": "{RAZORPAY_KEY_ID}",

    "amount": "{order['amount']}",

    "currency": "INR",

    "name": "Premium Subscription",

    "description": "AI Project Premium Plan",

    "order_id": "{order['id']}",

    "handler": function (response) {{

        alert(
            "Payment Successful!\\n\\n" +
            "Payment ID: " +
            response.razorpay_payment_id
        );

        console.log(response);

    }},

    "prefill": {{

        "name": "Test User",
        "email": "test@example.com",
        "contact": "9999999999"

    }},

    "theme": {{
        "color": "#3399cc"
    }},

    "modal": {{
        "ondismiss": function(){{
            console.log("Payment popup closed");
        }}
    }}
}};

var rzp = new Razorpay(options);

document.getElementById('pay-btn').onclick = function(e) {{
    rzp.open();
    e.preventDefault();
}}

</script>

</body>
</html>
"""
components.html(
    payment_html,
    height=700,
    scrolling=True
)

st.divider()

st.success("Razorpay Test Mode Enabled")

st.info("""
Testing Tips:

• Use Test Mode API Keys

• Test UPI ID:
success@razorpay

• Test Card:
4111 1111 1111 1111

Expiry:
12/30

CVV:
123

OTP:
Any 6 digits
""")