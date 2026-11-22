import streamlit as st
import streamlit.components.v1 as components

st.title("Razorpay Test")

RAZORPAY_KEY = "rzp_test_SZ1oLJy1yrd4xR"

if st.button("💳 Open Payment"):

    html = f"""
    <html>
    <head>
        <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
    </head>
    <body>

    <script>

    var options = {{
        "key": "{RAZORPAY_KEY}",
        "amount": "50000",
        "currency": "INR",
        "name": "Goal Planner",
        "description": "Test Payment",

        "handler": function (response) {{
            alert("Payment Successful");
        }}
    }};

    var rzp = new Razorpay(options);

    window.onload = function() {{
        rzp.open();
    }};

    </script>

    </body>
    </html>
    """

    components.html(html, height=780)