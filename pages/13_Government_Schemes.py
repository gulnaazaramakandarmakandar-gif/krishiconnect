import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Government Schemes",
    page_icon="🏛️",
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

/* ---------------- SCHEME CARDS ---------------- */

.scheme-card {

    background: rgba(255,255,255,0.92);

    padding: 25px;

    border-radius: 18px;

    margin-bottom: 20px;

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

st.title("🏛️ Government Schemes for Farmers")

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
🌾 Farmer Welfare & Support Programs
</h3>

<p>
Explore government schemes, subsidies, insurance,
credit support, and digital agriculture initiatives
designed to empower farmers across India.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

st.info(
    "Explore useful government schemes, benefits, and application links for farmers."
)

st.markdown("---")

# ---------------- PM-KISAN ----------------

st.markdown("""
<div class="scheme-card">

<h3>🌾 PM-KISAN Scheme</h3>

<p>
The Pradhan Mantri Kisan Samman Nidhi (PM-KISAN) scheme provides
financial assistance of ₹6000 per year to eligible farmers in three installments.
The scheme helps farmers manage agricultural expenses and household needs.
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🔗 Apply for PM-KISAN",
    "https://pmkisan.gov.in/"
)

st.markdown("---")

# ---------------- FASAL BIMA ----------------

st.markdown("""
<div class="scheme-card">

<h3>☂️ Pradhan Mantri Fasal Bima Yojana</h3>

<p>
This crop insurance scheme protects farmers against crop loss caused by
natural disasters, pests, and diseases. Farmers receive financial support
when crops are damaged.
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🔗 Apply for Crop Insurance",
    "https://pmfby.gov.in/"
)

st.markdown("---")

# ---------------- SOIL HEALTH CARD ----------------

st.markdown("""
<div class="scheme-card">

<h3>🌱 Soil Health Card Scheme</h3>

<p>
The Soil Health Card Scheme helps farmers understand soil quality
and nutrient levels. It provides recommendations for fertilizers
and crop management to improve productivity.
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🔗 Apply for Soil Health Card",
    "https://soilhealth.dac.gov.in/"
)

st.markdown("---")

# ---------------- E-NAM ----------------

st.markdown("""
<div class="scheme-card">

<h3>📈 e-NAM Market Portal</h3>

<p>
e-NAM (National Agriculture Market) is an online trading platform
that connects farmers with markets across India. It helps farmers
get better prices for their crops.
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🔗 Visit e-NAM",
    "https://www.enam.gov.in/"
)

st.markdown("---")

# ---------------- KCC ----------------

st.markdown("""
<div class="scheme-card">

<h3>💳 Kisan Credit Card (KCC)</h3>

<p>
Kisan Credit Card provides farmers with low-interest loans for
purchasing seeds, fertilizers, equipment, and other farming needs.
It ensures quick and easy access to credit.
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🔗 Apply for Kisan Credit Card",
    "https://www.myscheme.gov.in/schemes/kcc"
)

st.markdown("---")

# ---------------- FARMER HELPLINE ----------------

st.markdown("""
<div class="scheme-card">

<h3>📞 Farmer Helpline</h3>

<p>
Farmers can contact the national helpline for guidance related to
farming practices, schemes, subsidies, and agricultural support.
</p>

</div>
""", unsafe_allow_html=True)

st.success(
    "National Farmer Helpline: 1800-180-1551"
)

# ---------------- FARMER BENEFITS ----------------

st.markdown("---")

st.success("""
🚜 Benefits for Farmers

✔ Financial Assistance  
✔ Crop Insurance Protection  
✔ Easy Agricultural Loans  
✔ Better Market Connectivity  
✔ Soil Health Improvement  
✔ Government Subsidy Access
""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Government Support & Welfare System 🚜"
)

# ---------------- BACK TO DASHBOARD ----------------

st.markdown("---")

if st.button("⬅ Back to Dashboard"):

    st.switch_page("pages/1_Dashboard.py")