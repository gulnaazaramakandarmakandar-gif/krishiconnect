import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="News & Alerts",
    page_icon="📰",
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

/* ---------------- NEWS CARDS ---------------- */

.news-card {

    background: rgba(255,255,255,0.92);

    padding: 20px;

    border-radius: 18px;

    margin-bottom: 15px;

    box-shadow: 0px 4px 12px rgba(0,0,0,0.12);

    border-left: 6px solid #2e7d32;
}

/* ---------------- TEXT ---------------- */

p, label, div {

    color: #1f1f1f !important;

    font-size: 16px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("📰 News & Alerts")

# ---------------- HERO SECTION ----------------

st.markdown("""
<div style="
background: rgba(255,255,255,0.90);
padding: 25px;
border-radius: 18px;
box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
text-align:center;
">

<h3>
🌾 Agriculture News & Smart Alerts
</h3>

<p>
Stay updated with the latest agriculture news,
weather alerts, market changes, and farmer welfare updates.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

st.subheader("📢 Latest Agriculture Updates")

st.write("")

# ---------------- ALERTS ----------------

st.warning("⚠ Heavy rainfall expected in Shivamogga tomorrow.")

st.error("🚨 Tomato prices dropped by 5% in Hubli market.")

st.success("✅ Onion prices increased in Bengaluru market.")

st.info("ℹ Government announced new subsidy scheme for farmers.")

st.write("")

# ---------------- NEWS CARDS ----------------

news = [
    {
        "title": "🌾 New Irrigation Support Program",
        "content": "Government launched irrigation support for small farmers."
    },

    {
        "title": "☁ Rain Alert in Coastal Karnataka",
        "content": "Farmers advised to avoid harvesting during heavy rain."
    },

    {
        "title": "📈 Tomato Prices Increasing",
        "content": "Tomato demand increased in Bengaluru market."
    },

    {
        "title": "💰 PM-KISAN Installment Released",
        "content": "Farmers will receive new installment this week."
    }
]

# ---------------- DISPLAY NEWS ----------------

st.markdown("---")

st.subheader("🗞 Featured Agriculture News")

for item in news:

    st.markdown(f"""
    <div class="news-card">

    <h3>{item["title"]}</h3>

    <p>{item["content"]}</p>

    </div>
    """, unsafe_allow_html=True)

# ---------------- FARMER ADVISORY ----------------

st.markdown("---")

st.success("""
🚜 Smart Farmer Advisory

✔ Monitor market trends regularly  
✔ Follow weather alerts before harvesting  
✔ Use irrigation efficiently during summer  
✔ Compare crop prices across markets  
✔ Stay updated with government schemes
""")

# ---------------- DATE & TIME ----------------

st.markdown("---")

st.subheader("⏰ Last Updated")

st.success(
    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Agriculture News & Alert System 🚜"
)

# ---------------- BACK TO DASHBOARD ----------------

st.markdown("---")

if st.button("⬅ Back to Dashboard"):

    st.switch_page("pages/1_Dashboard.py")