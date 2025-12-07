import sqlite3
import pandas as pd

# Path to CSV
csv_path = "data/customer_support_tickets.csv"

# Load CSV into pandas
df = pd.read_csv(csv_path)

# Create SQLite database
conn = sqlite3.connect("customer_support.db")

# Write dataframe to SQL table
df.to_sql("tickets", conn, if_exists="replace", index=False)

conn.close()

print("Database created and data imported successfully.")
