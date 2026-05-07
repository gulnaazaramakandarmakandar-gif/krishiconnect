import streamlit as st
import pandas as pd
import sqlite3
import math
from datetime import datetime

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Cart & Wishlist",
    page_icon="🛒",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #f5fff5;
}

h1, h2, h3 {
    color: green;
}

[data-testid="stSidebar"] {
    background-color: #eaffea;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE CONNECTION ----------------

conn = sqlite3.connect(
    "database/krishiconnect.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ---------------- CREATE TABLES ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop TEXT,
    best_market TEXT,
    best_price INTEGER,
    distance REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS wishlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop TEXT,
    best_market TEXT,
    best_price INTEGER,
    distance REAL
)
""")

conn.commit()

# ---------------- TITLE ----------------

st.title("🛒 Smart Cart & Wishlist System")

st.subheader(
    "AI-Based Market Recommendation & Distance Analysis"
)

st.markdown("---")

# ---------------- LOAD DATA ----------------

df = pd.read_csv("data/crop_prices.csv")

# ---------------- MARKET LOCATIONS ----------------

markets = {
    "Davangere": (14.4661, 75.9238),
    "Hubli": (15.3647, 75.1240),
    "Belagavi": (15.8497, 74.4977),
    "Bengaluru": (12.9716, 77.5946),
    "Mysuru": (12.2958, 76.6394),
    "Mangaluru": (12.9141, 74.8560),
    "Shivamogga": (13.9299, 75.5681),
    "Vijayapura": (16.8302, 75.7100),
    "Ballari": (15.1394, 76.9214),
    "Kalaburagi": (17.3297, 76.8343)
}

# ---------------- SIDEBAR ----------------

st.sidebar.header("👨‍🌾 Farmer Information")

farmer_name = st.sidebar.text_input(
    "Farmer Name",
    "Farmer"
)

user_city = st.sidebar.selectbox(
    "📍 Select Your City",
    list(markets.keys())
)

# ---------------- SEARCH BAR ----------------

search = st.text_input("🔍 Search Crop")

if search:
    filtered_df = df[
        df["Crop"].str.contains(search, case=False)
    ]
else:
    filtered_df = df

# ---------------- PRODUCT SELECTION ----------------

# ---------------- SELECT PRODUCT ----------------

if filtered_df.empty:

    st.error("No crop found")

    st.stop()

crop = st.selectbox(
    "🌾 Select Product",
    filtered_df["Crop"].unique()
)

selected = df[df["Crop"] == crop]

# ---------------- SAFETY CHECK ----------------

if selected.empty:

    st.error("Crop data not available")

    st.stop()

# ---------------- MARKET PRICES ----------------

market_prices = {
    "Davangere": selected["Davangere"].values[0],
    "Hubli": selected["Hubli"].values[0],
    "Belagavi": selected["Belagavi"].values[0],
    "Bengaluru": selected["Bengaluru"].values[0],
    "Mysuru": selected["Mysuru"].values[0],
    "Mangaluru": selected["Mangaluru"].values[0],
    "Shivamogga": selected["Shivamogga"].values[0],
    "Vijayapura": selected["Vijayapura"].values[0],
    "Ballari": selected["Ballari"].values[0],
    "Kalaburagi": selected["Kalaburagi"].values[0]
}

# ---------------- BEST MARKET ----------------

best_market = max(
    market_prices,
    key=market_prices.get
)

best_price = market_prices[best_market]

# ---------------- DISTANCE FUNCTION ----------------

def calculate_distance(lat1, lon1, lat2, lon2):

    radius = 6371

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    distance = radius * c

    return round(distance, 2)

# ---------------- DISTANCE ----------------

lat1, lon1 = markets[user_city]
lat2, lon2 = markets[best_market]

distance = calculate_distance(
    lat1,
    lon1,
    lat2,
    lon2
)

# ---------------- TRANSPORT COST ----------------

transport_cost = round(distance * 5)

estimated_profit = best_price - transport_cost

# ---------------- METRICS ----------------

st.subheader("📊 Product Recommendation")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌾 Product", crop)

with col2:
    st.metric("🏆 Best Market", best_market)

with col3:
    st.metric("💰 Best Price", f"₹{best_price}")

st.write("")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("🚗 Distance", f"{distance} km")

with col5:
    st.metric(
        "🚚 Transport Cost",
        f"₹{transport_cost}"
    )

with col6:
    st.metric(
        "📈 Estimated Profit",
        f"₹{estimated_profit}"
    )

# ---------------- SMART RECOMMENDATION ----------------

st.markdown("---")

st.subheader("🤖 AI Recommendation")

if distance < 150:

    st.success(
        f"""
        Dear {farmer_name},

        Selling {crop} in {best_market} market
        is highly recommended.

        ✔ Higher Profit Potential
        ✔ Good Market Demand
        ✔ Transportation Distance is Reasonable
        """
    )

else:

    st.warning(
        f"""
        {best_market} market offers the highest price,
        but transportation distance is high.

        Consider nearby markets
        to reduce transport costs.
        """
    )

# ---------------- EXTRA SUGGESTION ----------------

if distance > 300:

    st.info("""
    🚜 Suggestion:

    Transportation distance is high.

    Consider nearby markets
    to reduce transportation expenses.
    """)

# ---------------- MARKET RANKINGS ----------------

st.markdown("---")

st.subheader("🏆 Market Rankings")

ranking = sorted(
    market_prices.items(),
    key=lambda x: x[1],
    reverse=True
)

for index, (market, price) in enumerate(ranking, start=1):

    st.markdown("---")

    col7, col8, col9, col10 = st.columns([1, 3, 2, 2])

    with col7:
        st.write(f"### #{index}")

    with col8:
        st.write(f"### 🏪 {market}")

    with col9:
        st.write(f"### ₹{price}")

    with col10:

        if st.button(
            f"🛒 Add",
            key=f"{market}_{index}"
        ):

            existing = cursor.execute(
                """
                SELECT * FROM cart
                WHERE crop = ? AND best_market = ?
                """,
                (crop, market)
            ).fetchone()

            if existing:

                st.warning(
                    f"{crop} from {market} already exists in Cart"
                )

            else:

                market_lat, market_lon = markets[market]

                market_distance = calculate_distance(
                    lat1,
                    lon1,
                    market_lat,
                    market_lon
                )

                cursor.execute(
                    """
                    INSERT INTO cart
                    (crop, best_market, best_price, distance)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        crop,
                        market,
                        price,
                        market_distance
                    )
                )

                conn.commit()

                st.success(
                    f"{crop} from {market} added to Cart"
                )

# ---------------- WISHLIST BUTTON ----------------

st.markdown("---")

if st.button("❤️ Add Best Market to Wishlist"):

    existing = cursor.execute(
        """
        SELECT * FROM wishlist
        WHERE crop = ?
        """,
        (crop,)
    ).fetchone()

    if existing:

        st.warning(
            f"{crop} already exists in Wishlist"
        )

    else:

        cursor.execute(
            """
            INSERT INTO wishlist
            (crop, best_market, best_price, distance)
            VALUES (?, ?, ?, ?)
            """,
            (
                crop,
                best_market,
                best_price,
                distance
            )
        )

        conn.commit()

        st.success(
            f"{crop} added to Wishlist"
        )

# ---------------- DISPLAY WISHLIST ----------------

st.markdown("---")

st.subheader("❤️ Wishlist")

wishlist_data = pd.read_sql_query(
    "SELECT * FROM wishlist",
    conn
)

if not wishlist_data.empty:

    st.dataframe(
        wishlist_data,
        use_container_width=True
    )

else:

    st.info("Wishlist is empty")

# ---------------- DISPLAY CART ----------------

st.markdown("---")

st.subheader("🛒 Cart")

cart_data = pd.read_sql_query(
    "SELECT * FROM cart",
    conn
)

if not cart_data.empty:

    st.dataframe(
        cart_data,
        use_container_width=True
    )

else:

    st.info("Cart is empty")

# ---------------- CLEAR BUTTONS ----------------

st.markdown("---")

col11, col12 = st.columns(2)

with col11:

    if st.button("🗑 Clear Wishlist"):

        cursor.execute("DELETE FROM wishlist")

        conn.commit()

        st.success("Wishlist Cleared")

        st.rerun()

with col12:

    if st.button("🗑 Clear Cart"):

        cursor.execute("DELETE FROM cart")

        conn.commit()

        st.success("Cart Cleared")

        st.rerun()

# ---------------- DOWNLOAD REPORT ----------------

st.markdown("---")

st.subheader("📄 Download Recommendation Report")

report_df = pd.DataFrame({
    "Product": [crop],
    "Best Market": [best_market],
    "Best Price": [best_price],
    "Distance": [distance],
    "Transport Cost": [transport_cost],
    "Estimated Profit": [estimated_profit],
    "Generated On": [datetime.now()]
})

csv = report_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Report",
    data=csv,
    file_name="market_report.csv",
    mime="text/csv"
)

# ---------------- LAST UPDATED ----------------

st.info(
    f"⏰ Last Updated: "
    f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🌾 KrishiConnect | Smart Farmer Decision Support System 🚜"
)

# ---------------- CLOSE DATABASE ----------------

conn.close()