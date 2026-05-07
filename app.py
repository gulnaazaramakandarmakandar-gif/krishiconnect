import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="KrishiConnect",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- HIDE SIDEBAR ----------------

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

.stApp {
    background-color: #f5fff5;
}

h1, h2, h3 {
    text-align: center;
    color: green;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🌾 KrishiConnect")

st.subheader(
    "Smart Farmer Market Information & Decision Support System"
)

st.markdown("---")

st.success("""
Helping Farmers:
✔ Compare Market Prices  
✔ Find Best Markets  
✔ Analyze Crop Trends  
✔ Get Weather Alerts  
✔ Improve Profit Decisions
""")

st.markdown("---")

# ---------------- CONTINUE ----------------

st.info("Do you want to continue?")

col1, col2 = st.columns(2)

with col1:

    if st.button("✅ Yes", use_container_width=True):

        st.switch_page("pages/1_Dashboard.py")

with col2:

    if st.button("❌ No", use_container_width=True):

        st.warning("Thank you for visiting KrishiConnect 🌱")