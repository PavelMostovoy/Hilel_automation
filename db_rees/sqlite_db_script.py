import sqlite3
con = sqlite3.connect('local_db.db')


cur = con.cursor()

# Create table
table_name = "stock_1"
query = "CREATE TABLE if not exists " + table_name + " (id integer)"
cur.execute(query)

sql_request = '''CREATE TABLE secondary
               (date text, trans text, id real, qty real, price real)'''

cur.execute(sql_request)

# Insert a row of data
# cur.execute(f"INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

con.close()