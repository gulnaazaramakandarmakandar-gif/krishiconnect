import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Weather Information",
    page_icon="☁",
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

/* ---------------- TABLES ---------------- */

.stDataFrame {

    background-color: rgba(255,255,255,0.95);

    border-radius: 15px;

    padding: 10px;
}

/* ---------------- INPUTS ---------------- */

.stTextInput input,
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

st.title("☁ Weather Information")

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
🌦 Smart Weather Monitoring System
</h3>

<p>
Monitor weather conditions across Karnataka markets
to help farmers make safe harvesting and irrigation decisions.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

st.subheader(
    "Weather Conditions Across Karnataka Markets"
)

st.markdown("---")

# ---------------- LOAD DATA ----------------

weather_df = pd.read_csv(
    "data/weather_data.csv"
)

# ---------------- SEARCH CITY ----------------

search = st.text_input("🔍 Search City")

if search:
    filtered_df = weather_df[
        weather_df["City"].str.contains(
            search,
            case=False
        )
    ]
else:
    filtered_df = weather_df

# ---------------- DISPLAY DATA ----------------

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)

# ---------------- CITY SELECTION ----------------

city = st.selectbox(
    "📍 Select City",
    filtered_df["City"]
)

selected = weather_df[
    weather_df["City"] == city
]

# ---------------- WEATHER DETAILS ----------------

temperature = selected["Temperature"].values[0]
humidity = selected["Humidity"].values[0]
rain = selected["Rain"].values[0]
wind = selected["WindSpeed"].values[0]
condition = selected["Condition"].values[0]

# ---------------- METRICS ----------------

st.markdown("---")

st.subheader("📊 Weather Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌡 Temperature",
        f"{temperature}°C"
    )

with col2:
    st.metric(
        "💧 Humidity",
        f"{humidity}%"
    )

with col3:
    st.metric(
        "💨 Wind Speed",
        f"{wind} km/h"
    )

# ---------------- CONDITION ----------------

st.markdown("---")

st.subheader(f"☁ Weather in {city}")

st.info(
    f"""
    🌤 Weather Condition: {condition}
    
    🌧 Rain Expected: {rain}
    """
)

# ---------------- ALERTS ----------------

if rain == "Yes":

    st.warning("""
    ⚠ Rain Alert
    
    Farmers are advised to avoid harvesting
    during heavy rainfall.
    """)

if temperature > 32:

    st.error("""
    ☀ Heat Alert
    
    High temperature detected.
    
    Ensure proper irrigation for crops.
    """)

# ---------------- WEATHER SUMMARY ----------------

st.markdown("---")

st.success(f"""
🌾 Farming Recommendation for {city}

✔ Monitor crop moisture regularly  
✔ Check irrigation schedules  
✔ Follow weather alerts before harvesting  
✔ Protect crops during extreme heat/rainfall
""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Smart Weather Monitoring System 🚜"
)

# ---------------- BACK TO DASHBOARD ----------------

st.markdown("---")

if st.button("⬅ Back to Dashboard"):

    st.switch_page("pages/1_Dashboard.py")