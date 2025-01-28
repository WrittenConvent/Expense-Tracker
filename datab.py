import sqlite3

#Create a .db file if it already doesn' exist
conn=sqlite3.connect("cost_tracker.db")

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS expense
             (date text, name text , qty real, price real)''')
print("1 to view transactions at a specific date")
print("2 for clear table")
print("3 to add another row")
op = int(input("Option: "))
if op==1:
    datem = input("Enter the date (YYYY-MM-DD) to view transactions: ")
    cursor.execute("SELECT * FROM expense WHERE date=?", (datem,))
    rows=cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("no transactions on {datem}")
elif op==2:
    cursor.execute("DELETE FROM expense")
    conn.commit()
elif op==3:
    column_name = input("Enter column name=")
    data_type = input("Enter data type in uppercase=")

    try:
        cursor.execute(f"ALTER TABLE expense ADD COLUMN {column_name} {data_type}")
        print(f"Column '{column_name}' added successfully.")
    except sqlite3.OperationalError:
        print(f"Column '{column_name}' already exists or cannot be added.")
    conn.commit()
else:
    print("Invalid Option")


# Close the connection
conn.close()

