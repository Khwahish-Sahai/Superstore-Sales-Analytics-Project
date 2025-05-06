import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your MySQL credentials
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Khwahishsahai786",
    database="sales_project"
)
cursor = conn.cursor()
if conn.is_connected():
        print("✅ Successfully connected to MySQL database!")
else:
    print("❌ Connection failed.")
import sqlalchemy
import pymysql

print("✅ SQLAlchemy and PyMySQL are installed and ready!")
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Khwahishsahai786@localhost/sales_project")

import pandas as pd

query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

df = pd.read_sql(query, engine)

print(df)

df.plot(kind='bar', x='product', y='revenue', color='tomato', legend=False)


plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout() 


plt.show()

plt.savefig("sales_revenue_chart.png")

df.to_csv("sales_summary.csv", index=False)
