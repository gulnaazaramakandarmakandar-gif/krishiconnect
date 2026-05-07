import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="About KrishiConnect",
    page_icon="ℹ",
    layout="wide"
)

# ---------------- UI STYLING ----------------

st.markdown("""
<style>

/* ---------------- MAIN BACKGROUND ---------------- */

.stApp {

    background:
    linear-gradient(
        rgba(245,255,245,0.94),
        rgba(245,255,245,0.94)
    ),

    url("https://images.unsplash.com/photo-1500937386664-56d1dfef3854?q=80&w=1974&auto=format&fit=crop");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ---------------- HIDE SIDEBAR ---------------- */

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* ---------------- HEADERS ---------------- */

h1 {

    color: #1b5e20 !important;

    text-align: center;

    font-size: 42px !important;

    font-weight: bold !important;
}

h2, h3 {

    color: #2e7d32 !important;
}

/* ---------------- BUTTONS ---------------- */

div.stButton > button {

    background: linear-gradient(
        to right,
        #2e7d32,
        #43a047
    );

    color: white !important;

    border: none;

    border-radius: 14px;

    padding: 12px;

    font-size: 16px;

    font-weight: bold;

    width: 100%;

    transition: 0.3s;

    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

div.stButton > button:hover {

    background: linear-gradient(
        to right,
        #1b5e20,
        #2e7d32
    );

    transform: scale(1.02);
}

/* ---------------- TEXT ---------------- */

p, label, div {

    color: #1f1f1f !important;

    font-size: 17px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("ℹ About KrishiConnect")

# ---------------- HERO SECTION ----------------

st.markdown("""
<div style="
background: rgba(255,255,255,0.90);
padding: 30px;
border-radius: 18px;
box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
text-align:center;
">

<h3>
🌾 Smart Agriculture Support Platform
</h3>

<p>
KrishiConnect is an AI-powered farmer support platform
developed to help farmers make smarter agricultural decisions.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- ABOUT CONTENT ----------------

st.markdown("""
## 🚜 About the Project

KrishiConnect is a farmer support platform developed
for hackathon purposes.

The platform helps farmers by providing:

✔ Live Market Price Analysis  
✔ Crop Price Trend Monitoring  
✔ Weather Information & Alerts  
✔ AI-Based Market Recommendations  
✔ Profit Calculation Support  
✔ Government Scheme Awareness  
✔ Smart Cart & Wishlist System  

The goal of KrishiConnect is to empower farmers
through technology and improve agricultural decision-making.
""")

# ---------------- FEATURES ----------------

st.markdown("---")

st.subheader("🌱 Key Features")

col1, col2 = st.columns(2)

with col1:

    st.success("""
    📈 Market Price Tracking
    
    ☁ Weather Monitoring
    
    🤖 AI Recommendations
    
    💰 Profit Optimization
    """)

with col2:

    st.success("""
    📰 Agriculture News
    
    🏛 Government Schemes
    
    🛒 Smart Cart System
    
    🚜 Farmer Decision Support
    """)

# ---------------- MISSION ----------------

st.markdown("---")

st.info("""
🌾 Mission

To support farmers using smart technology,
data analysis, and AI-powered agricultural solutions.
""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Empowering Farmers Through Technology 🚜"
)

# ---------------- BACK TO DASHBOARD ----------------

st.markdown("---")

if st.button("⬅ Back to Dashboard"):

    st.switch_page("pages/1_Dashboard.py")