import sqlite3

conn = sqlite3.connect("database/krishiconnect.db")

cursor = conn.cursor()

# ---------------- CART TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop TEXT,
    best_market TEXT,
    best_price INTEGER
)
""")

# ---------------- WISHLIST TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS wishlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop TEXT,
    best_market TEXT,
    best_price INTEGER
)
""")

conn.commit()

conn.close()

print("Database Created Successfully")