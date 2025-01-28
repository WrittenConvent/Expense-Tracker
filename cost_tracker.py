import sys
import os
import sqlite3
from datetime import datetime

conn=sqlite3.connect("expense.db")
ex=conn.cursor()
x=datetime.now().date().isoformat() #change date to iso format

ex.execute('''CREATE TABLE IF NOT EXISTS expense
             (date text, name text, qty real, price real)''')

while True:
    a=input("Enter 1 to stop input\nname=") #take input
    if a=='1':
        break
    
    b=input("price=")
    c=input("quantity=")
    
    ex.execute("INSERT INTO spending (date, name, type, qty, price) VALUES (?, ?, ?, ?, ?)", (x, a, float(c), float(b)))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()