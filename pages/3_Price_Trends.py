import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Price Trends",
    page_icon="📊",
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

/* ---------------- TEXT ---------------- */

p, label, div {

    color: #1f1f1f !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("📊 Price Trends")

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
📈 Weekly Crop Price Trend Analysis
</h3>

<p>
Analyze daily crop price fluctuations and understand
market demand patterns to make better selling decisions.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- DATA ----------------

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

prices = [2200, 2300, 2400, 2500, 2450, 2550, 2600]

trend_df = pd.DataFrame({
    "Day": days,
    "Tomato": prices
})

# ---------------- METRICS ----------------

st.markdown("---")

st.subheader("📊 Weekly Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌾 Crop",
        "Tomato"
    )

with col2:
    st.metric(
        "📈 Highest Price",
        "₹2600"
    )

with col3:
    st.metric(
        "📉 Lowest Price",
        "₹2200"
    )

# ---------------- CHART ----------------

st.markdown("---")

st.subheader("📉 Tomato Price Trend")

st.line_chart(
    trend_df.set_index("Day"),
    use_container_width=True
)

# ---------------- INSIGHT ----------------

st.markdown("---")

st.success("""
🌾 Market Insight

Tomato prices are showing an increasing trend this week.

🚜 Farmers are advised to monitor market demand
and consider selling during peak price periods.
""")

# ---------------- TABLE ----------------

st.markdown("---")

st.subheader("📋 Weekly Price Table")

st.dataframe(
    trend_df,
    use_container_width=True,
    height=300
)

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Smart Crop Trend Analysis 🚜"
)

# ---------------- BACK TO DASHBOARD ----------------

st.markdown("---")

if st.button("⬅ Back to Dashboard"):

    st.switch_page("pages/1_Dashboard.py")