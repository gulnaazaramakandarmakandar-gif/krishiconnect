import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Profit Calculator",
    page_icon="💰",
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

/* ---------------- INPUT BOXES ---------------- */

.stNumberInput input {

    border-radius: 10px !important;

    border: 2px solid #66bb6a !important;
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

st.title("💰 Profit Calculator")

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
📈 Smart Farmer Profit Estimation
</h3>

<p>
Calculate expected income and estimated profit
based on crop price, quantity, and transportation expenses.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- INPUT SECTION ----------------

st.subheader("🧮 Enter Details")

crop_price = st.number_input(
    "🌾 Enter Crop Price per Quintal",
    min_value=0
)

quantity = st.number_input(
    "📦 Enter Quantity",
    min_value=0
)

transport_cost = st.number_input(
    "🚚 Enter Transport Cost",
    min_value=0
)

# ---------------- CALCULATIONS ----------------

total_income = crop_price * quantity

profit = total_income - transport_cost

# ---------------- RESULTS ----------------

st.markdown("---")

st.subheader("📊 Profit Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Income",
        f"₹{total_income}"
    )

with col2:
    st.metric(
        "🚚 Transport Cost",
        f"₹{transport_cost}"
    )

with col3:
    st.metric(
        "📈 Estimated Profit",
        f"₹{profit}"
    )

# ---------------- SMART INSIGHT ----------------

st.markdown("---")

if profit > 0:

    st.success(f"""
    🌾 Profit Insight
    
    Farmers can expect an estimated profit of ₹{profit}.
    
    ✔ Current market conditions appear profitable.
    """)

else:

    st.warning("""
    ⚠ Low Profit Alert
    
    Transportation or crop pricing may reduce profit.
    
    Consider choosing a nearby market.
    """)

# ---------------- FARMER TIPS ----------------

st.markdown("---")

st.info("""
🚜 Smart Farming Tips

✔ Compare market prices before selling  
✔ Reduce unnecessary transportation costs  
✔ Monitor weather conditions regularly  
✔ Use AI predictions for better planning
""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Smart Profit Optimization System 🚜"
)

# ---------------- BACK TO DASHBOARD ----------------

st.markdown("---")

if st.button("⬅ Back to Dashboard"):

    st.switch_page("pages/1_Dashboard.py")