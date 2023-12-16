# init_db.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT, address TEXT, city TEXT, zip TEXT)')
print("Table created successfully")
conn.close()
