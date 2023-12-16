# init_db.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE employees (name TEXT, address TEXT, city TEXT, state TEXT, zip TEXT, wage TEXT)')
print("Table created successfully")
conn.close()
