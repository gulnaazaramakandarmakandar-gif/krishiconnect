import streamlit as st
from datetime import datetime
from utils.style import apply_custom_css

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- APPLY UI ----------------

apply_custom_css()

# ---------------- HIDE SIDEBAR ----------------

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------

st.title("🌾 KrishiConnect Dashboard")

st.markdown("""
<div style="
background: rgba(255,255,255,0.88);
padding: 25px;
border-radius: 18px;
box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
text-align:center;
">

<h3>
🚜 Smart Agriculture Platform for Farmers
</h3>

<p>
Helping farmers make better decisions using
AI-powered market analysis, weather monitoring,
profit optimization, and government support systems.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

st.success("Choose a feature below")

# ---------------- DATE ----------------

current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

st.info(f"⏰ Current Date & Time: {current_time}")

# ---------------- METRICS ----------------

st.markdown("## 📊 Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌾 Crops", "10")

with col2:
    st.metric("🏪 Markets", "10")

with col3:
    st.metric("🤖 AI Features", "5")

with col4:
    st.metric("👨‍🌾 Farmers Supported", "1000+")

st.markdown("---")

# ---------------- FIRST ROW ----------------

st.subheader("📌 Core Features")

col5, col6, col7 = st.columns(3)

with col5:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>📈 Market Prices</h3>
    <p>Compare crop prices across markets</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Market Prices",
        use_container_width=True
    ):
        st.switch_page("pages/1_Market_Prices.py")

with col6:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>📊 Price Trends</h3>
    <p>Analyze crop price trends visually</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Price Trends",
        use_container_width=True
    ):
        st.switch_page("pages/3_Price_Trends.py")

with col7:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>☁ Weather</h3>
    <p>Monitor weather conditions & alerts</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Weather",
        use_container_width=True
    ):
        st.switch_page("pages/5_Weather.py")

st.write("")

# ---------------- SECOND ROW ----------------

col8, col9, col10 = st.columns(3)

with col8:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>🤖 Prediction Bot</h3>
    <p>AI-based crop market prediction system</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Prediction Bot",
        use_container_width=True
    ):
        st.switch_page("pages/7_Prediction_Bot.py")

with col9:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>💰 Profit Calculator</h3>
    <p>Estimate transportation & selling profit</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Profit Calculator",
        use_container_width=True
    ):
        st.switch_page("pages/11_Profit_Calculator.py")

with col10:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>🛒 Cart & Wishlist</h3>
    <p>Smart market recommendation system</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Cart & Wishlist",
        use_container_width=True
    ):
        st.switch_page("pages/15_Cart_and_Wishlist.py")

st.write("")

# ---------------- THIRD ROW ----------------

col11, col12 = st.columns(2)

with col11:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>📰 News & Alerts</h3>
    <p>Latest agriculture updates & notifications</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open News & Alerts",
        use_container_width=True
    ):
        st.switch_page("pages/12_News_Alerts.py")

with col12:

    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
    <h3>🏛️ Government Schemes</h3>
    <p>Farmer welfare schemes & application links</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Government Schemes",
        use_container_width=True
    ):
        st.switch_page("pages/13_Government_Schemes.py")

# ---------------- TIPS ----------------

st.markdown("---")

st.subheader("🌱 Daily Farming Tips")

tips = [
    "💧 Irrigate crops early morning.",
    "🌾 Compare market prices before selling.",
    "☁ Check weather updates regularly.",
    "📈 Tomato prices are increasing this week.",
    "🚜 Use organic fertilizers for better yield."
]

for tip in tips:
    st.success(tip)

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Empowering Farmers Through Technology 🚜"
)