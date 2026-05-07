import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Prediction Bot",
    page_icon="🤖",
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

/* ---------------- METRIC CARDS ---------------- */

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.95);

    border-radius: 18px;

    padding: 15px;

    border-left: 6px solid #2e7d32;

    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
}

/* ---------------- INPUTS ---------------- */

.stSelectbox div {

    border-radius: 10px !important;

    border: 2px solid #66bb6a !important;
}

/* ---------------- TEXT ---------------- */

p, label, div {

    color: #1f1f1f !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🤖 Prediction Bot")

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
📈 AI-Based Market Prediction System
</h3>

<p>
Analyze crop prices across markets and predict
future market trends to help farmers maximize profit.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- LOAD DATA ----------------

df = pd.read_csv("data/crop_prices.csv")

# ---------------- SELECT CROP ----------------

crop = st.selectbox(
    "🌾 Select Crop",
    df["Crop"]
)

selected = df[df["Crop"] == crop]

# ---------------- MARKET DATA ----------------

markets = [
    "Davangere",
    "Hubli",
    "Belagavi",
    "Bengaluru"
]

prices = {
    "Davangere": selected["Davangere"].values[0],
    "Hubli": selected["Hubli"].values[0],
    "Belagavi": selected["Belagavi"].values[0],
    "Bengaluru": selected["Bengaluru"].values[0]
}

# ---------------- BEST MARKET ----------------

best_market = max(prices, key=prices.get)

highest_price = prices[best_market]

average_price = sum(prices.values()) / len(prices)

# ---------------- METRICS ----------------

st.markdown("---")

st.subheader("📊 Prediction Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌾 Crop",
        crop
    )

with col2:
    st.metric(
        "🏆 Best Market",
        best_market
    )

with col3:
    st.metric(
        "💰 Highest Price",
        f"₹{highest_price}"
    )

# ---------------- RECOMMENDATION ----------------

st.markdown("---")

st.success(
    f"""
    🌾 Best Market Recommendation
    
    🏪 Best market for selling {crop} is {best_market}
    
    💰 Expected Selling Price: ₹{highest_price}
    """
)

# ---------------- PREDICTION LOGIC ----------------

st.markdown("---")

st.subheader("🤖 AI Prediction")

if highest_price > average_price:

    st.info("""
    📈 Prediction Result
    
    Crop prices are showing an increasing trend.
    
    Farmers may get better profit tomorrow.
    """)

else:

    st.warning("""
    📉 Prediction Result
    
    Crop prices may decrease tomorrow.
    
    Farmers are advised to monitor the market carefully.
    """)

# ---------------- MARKET PRICE TABLE ----------------

st.markdown("---")

st.subheader("📋 Market Price Comparison")

price_df = pd.DataFrame({
    "Market": list(prices.keys()),
    "Price": list(prices.values())
})

price_df.index = price_df.index + 1

st.dataframe(
    price_df,
    use_container_width=True,
    height=300
)

# ---------------- INSIGHT ----------------

st.markdown("---")

st.success("""
🚜 Smart Farmer Insight

✔ Monitor market prices regularly  
✔ Compare prices across markets  
✔ Sell crops during peak demand periods  
✔ Use prediction systems for better planning
""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | AI Market Prediction System 🚜"
)

# ---------------- BACK TO DASHBOARD ----------------

st.markdown("---")

if st.button("⬅ Back to Dashboard"):

    st.switch_page("pages/1_Dashboard.py")