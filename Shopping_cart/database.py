import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY AUTOINCREMENT, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')

conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')

conn.execute('''INSERT INTO categories VALUES ( 1, 'Ethnic')''')
conn.execute('''INSERT INTO categories VALUES ( 2, 'Dresses')''')
conn.execute('''INSERT INTO categories VALUES ( 3, 'Tops')''')
conn.execute('''INSERT INTO categories VALUES ( 4, 'Bottomwear')''')
conn.execute('''INSERT INTO categories VALUES ( 5, 'Sweaters')''')

conn.execute('''INSERT INTO products
VALUES (1,'red lehenga', 5000, 'high quality bridal lehenga','products/lehenga1.jpg', 3, 1)''')

conn.commit()
conn.close()

