import sqlite3

#Open database
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('''select * from users''')
categoryData = cur.fetchall()
print(categoryData)
conn.close()
