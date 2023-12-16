# app.py
# Tutorials Point Python SQLite3 tutorial

import sqlite3

conn = sqlite3.connect('jacksons.db')

conn.execute('''CREATE TABLE IF NOT EXISTS brothers
         (id INT PRIMARY KEY     NOT NULL,
         name           TEXT    NOT NULL,
         age            INT     NOT NULL,
         address        CHAR(50),
         salary         REAL);''')

print ("Table created successfully")

conn.execute("INSERT INTO brothers (id, name, age, address, salary) \
      VALUES (1, 'Steve', 49, 'Nampa', 80000.00 )");

conn.execute("INSERT INTO brothers (id, name, age, address, salary) \
      VALUES (2, 'Jared', 48, 'Woods Cross', 75000.00 )");

conn.execute("INSERT INTO brothers (id, name, age, address, salary) \
      VALUES (3, 'Mike', 46, 'Blackfoot', 32000.00 )");

conn.execute("INSERT INTO brothers (id, name, age, address, salary) \
      VALUES (4, 'Gabe', 44, 'Chicago', 95000.00 )");

print ("Records created successfully\n")

cursor = conn.execute("SELECT id, name, address, salary FROM brothers")

for row in cursor:
   print ("Id = ", row[0])
   print ("Name = ", row[1])
   print ("Address = ", row[2])
   print ("Salary = ", row[3], "\n")

print ("Operation done successfully")

conn.commit()
conn.close()



