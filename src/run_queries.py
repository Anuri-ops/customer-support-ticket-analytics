import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("customer_support.db")

# 1. Tickets by support channel
query_channel = """
SELECT [Ticket Channel] AS channel,
       COUNT(*) AS total_tickets
FROM tickets
GROUP BY [Ticket Channel]
ORDER BY total_tickets DESC;
"""
tickets_by_channel = pd.read_sql_query(query_channel, conn)
print("\nTickets by channel:")
print(tickets_by_channel)

# 2. Average satisfaction by channel
query_satisfaction = """
SELECT [Ticket Channel] AS channel,
       AVG([Customer Satisfaction Rating]) AS avg_satisfaction
FROM tickets
WHERE [Customer Satisfaction Rating] IS NOT NULL
GROUP BY [Ticket Channel]
ORDER BY avg_satisfaction DESC;
"""
satisfaction_by_channel = pd.read_sql_query(query_satisfaction, conn)
print("\nAverage satisfaction by channel:")
print(satisfaction_by_channel)

# 3. Average time to resolution by priority
query_resolution = """
SELECT [Ticket Priority] AS priority,
       AVG([Time to Resolution]) AS avg_resolution_hours,
       COUNT(*) AS tickets
FROM tickets
WHERE [Time to Resolution] IS NOT NULL
GROUP BY [Ticket Priority]
ORDER BY avg_resolution_hours DESC;
"""
resolution_by_priority = pd.read_sql_query(query_resolution, conn)
print("\nAverage time to resolution (hours) by priority:")
print(resolution_by_priority)

# Simple bar chart: tickets by channel
tickets_by_channel.plot(kind="bar", x="channel", y="total_tickets",
                        title="Tickets by Support Channel", legend=False)
plt.xlabel("Channel")
plt.ylabel("Number of Tickets")
plt.tight_layout()
plt.savefig("images/tickets_by_channel.png")
plt.show()

conn.close()
