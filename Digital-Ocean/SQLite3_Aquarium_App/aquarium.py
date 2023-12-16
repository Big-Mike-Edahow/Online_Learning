# aquarium.py

import sqlite3
from contextlib import closing

connection = sqlite3.connect("aquarium.db")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS fish")
cursor.execute("CREATE TABLE IF NOT EXISTS fish (name TEXT, species TEXT, tank INT)")

cursor.execute("INSERT INTO fish VALUES ('Sammy', 'Shark', '1')")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'Cuttlefish', '7')")

rows = cursor.execute("SELECT name, species, tank FROM fish").fetchall()
print(rows)

# Select fish from fish table and print the tuple.

fish = "Jamie"
rows = cursor.execute(
    "SELECT name, species, tank FROM fish WHERE name = ?", (fish,),).fetchall()
print(rows)

# Update moved_fish in fish table.

new_tank = 2
moved_fish = "Sammy"
cursor.execute(
    "UPDATE fish SET tank = ? WHERE name = ?",
    (new_tank, moved_fish)
)

rows = cursor.execute("SELECT name, species, tank FROM fish").fetchall()
print(rows)

# Delete released_fish from the fish table.

released_fish = "Sammy"
cursor.execute(
    "DELETE FROM fish WHERE name = ?",
    (released_fish,)
)

# Print out the individual items from the cursor object.

rows = cursor.execute("SELECT name, species, tank FROM fish").fetchall()

print("Name: \t", rows[0][0])
print("Species:", rows[0][1])
print("Tank: \t", rows[0][2])


# Use with to automatically close connection and cursor objects:

with closing(sqlite3.connect("aquarium.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)

