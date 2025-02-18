import sqlite3

conn = sqlite3.connect('database.db')

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS users 
                (userId integer primary key autoincrement,
  		password TEXT,
		email TEXT unique,
		firstName TEXT,
		lastName TEXT,
		role TEXT
		)''')
except:
    pass
try:
    conn.execute('''CREATE TABLE IF NOT EXISTS products
                (productId INTEGER primary key autoincrement,
		name TEXT,
		price REAL,
		image TEXT,
		mft DATE,
		exp DATE,
		stock INTEGER,
		categoryId INTEGER,
        unit TEXT,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')
except:
    pass
try:
    conn.execute('''CREATE TABLE IF NOT EXISTS kart
		(cartId INTEGER PRIMARY KEY AUTOINCREMENT,
		userId Integer,
		productId INTEGER,
        name TEXT,
        price REAL,
        quantity INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')
except:
    pass

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS orders (
        orderId INTEGER PRIMARY KEY AUTOINCREMENT,
        userId INTEGER,
        name TEXT,
        price REAL,
        quantity INTEGER,
        date DATE,
        productId Integer
    )''')
except:
    pass

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS requests (
        requestId INTEGER PRIMARY KEY AUTOINCREMENT,
        requestType TEXT,
        categoryId INTEGER,
        productId INTEGER,
        oldName TEXT,
        name TEXT,
        price REAL,
		image TEXT,
		mft DATE,
		exp DATE,
		stock INTEGER,
        userName TEXT,
        userId INTEGER,
        unit TEXT,
        FOREIGN KEY (categoryId) REFERENCES categories(categoryId),
        FOREIGN KEY (productId) REFERENCES products(productId),
        FOREIGN KEY (userId) REFERENCES users(userId)
    )''')
except:
    pass

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT UNIQUE,
        image TEXT
		)''')
except:
    pass

def create_admin_user():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    admin_user = (
        1,
        'as@as.as', #admin-email
        'admin',  
        'admin',  
        'as',  #admin-password
        'admin'  
    )

    try:
        cursor.execute('''INSERT INTO users (userId, email, firstName, lastName, password, role) 
                        VALUES (?, ?, ?, ?, ?, ?)''', admin_user)

        connection.commit()
        print("Admin user created successfully.")
    except sqlite3.Error as error:
        print(f"Error creating admin user: {error}")
        connection.rollback()
    finally:
        connection.close()

create_admin_user()