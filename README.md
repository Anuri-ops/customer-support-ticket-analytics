📊 **CUSTOMER SUPPORT TICKET ANALYTICS — SQL + PYTHON**

This project analyses a customer support ticket dataset to understand patterns in ticket volume, customer satisfaction, and support performance across different communication channels.

The workflow includes turning raw CSV data into a SQLite database, running SQL queries for insights, and visualising results using Python.



🗂 **DATASET**

**Source**: Kaggle — Customer Support Tickets Dataset

**Format**: CSV

Used to simulate real-world support analytics: channel performance, satisfaction levels, resolution efficiency, and ticket prioritisation.



🧰 **TOOLS & TECHNOLOGIES**

**CATEGORY	TECHNOLOGY**
  Database	SQLite
  Querying	SQL
  Language	Python
  Libraries	Pandas, Matplotlib
  Environment	VS Code



📁 **PROJECT STRUCTURE**

customer-support-ticket-analytics/
│
├── data/                           # Raw dataset

│   └── customer_support_tickets.csv
├── images/                         # Generated visual outputs

│   └── tickets_by_channel.png
├── src/

│   ├── setup_database.py           # Creates SQLite database from CSV
│   └── run_queries.py              # Runs SQL and visualisations

├── customer_support.db             # SQLite database file

└── README.md                       # Project documentation



🚀 **HOW TO RUN**

1️⃣ Install required libraries:
python -m pip install pandas matplotlib

2️⃣ Create the database:
python src/setup_database.py

3️⃣ Run analysis and generate visual output:
python src/run_queries.py



📈 **OUTPUT**

Tickets by Support Channel
<img src="images/tickets_by_channel.png" width="450">



🔍 **INSIGHTS**

Support channels receive varying volumes of requests.
Customer satisfaction and resolution time vary depending on the support method.
Insight into channel usage can guide resource allocation and workflow optimisation.



🧠 **SKILLS**

Data loading and cleaning

SQL querying and relational database design

Python data analysis

Visual storytelling with charts

Project structuring and documentation

Git/GitHub readiness



📌 **FUTURE IMPROVEMENTS**

Add an interactive dashboard (Streamlit, Tableau, or Power BI)

Build a prediction model (e.g., resolution time or satisfaction)

Add an automated reporting pipeline


If you find this useful or have suggestions, feel free to fork the repository or open an issue!

🔗 Author

**Anuri Nwagbara**
