# 🎟️ Customer Support Ticket Analytics — SQL + Python  

This project analyses a synthetic customer support ticket dataset to explore patterns in:
- Ticket volume across support channels  
- Customer satisfaction  
- Resolution performance and priority trends  

Raw CSV data is converted into a SQLite database, queried with SQL, and visualised using Python.

---

## 📂 Dataset  

**Source:** Kaggle — *Customer Support Tickets Dataset*  
**Format:** CSV  

The dataset simulates real-world support analytics such as:
- Channel usage
- Ticket prioritisation
- Satisfaction levels
- Resolution efficiency  

---

## 🛠️ Tools & Technologies  

| Category | Technology |
|---------|------------|
| Database | SQLite |
| Query Language | SQL |
| Programming Language | Python |
| Python Libraries | Pandas, Matplotlib |
| Environment | VS Code |

---

## 📁 Project Structure  


```
customer-support-ticket-analytics/
│
├── data/
│   └── customer_support_tickets.csv
│
├── images/
│   └── tickets_by_channel.png
│
├── src/
│   ├── setup_database.py      # Creates SQLite database from CSV
│   └── run_queries.py         # Runs SQL queries and visualisations
│
├── customer_support.db        # SQLite database file
└── README.md                  # Project documentation

```

---

### ▶️ How to Run

1. **Install required libraries**

   ```sh
   python -m pip install pandas matplotlib
   ```

2. **Create the database**

   ```sh
   python src/setup_database.py
   ```

3. **Run SQL queries and generate visual output**

   ```sh
   python src/run_queries.py
   ```

---

### 📈 Sample Output

> **Tickets Chart**

<img src="images/tickets_by_channel.png" width="400"/>

---

### 🔍 Insights

* Support channels receive varying request volumes.
* Satisfaction levels differ depending on the customer contact method.
* Resolution efficiency varies by priority category.
* Channel data can help optimise staffing and customer support workflows.

---

### 🧠 Skills Demonstrated

* Data cleaning and preparation
* SQL querying and relational schema fundamentals
* Python data analysis with Pandas
* Chart visualisation using Matplotlib
* Project structure and documentation
* Git & GitHub version control

---

### 🚀 Future Improvements

* Add an interactive dashboard (Streamlit, Tableau, or Power BI)
* Build a predictive model (resolution time or CSAT scoring)
* Automate reporting pipeline

---


---


If you find this useful or have suggestions, feel free to fork the repository or open an issue!

---

### 🔗 Author

**Anuri N. C. Nwagbara**
