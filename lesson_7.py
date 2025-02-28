import sqlite3


def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_product(db_name, product):
    sql = '''INSERT INTO products
    (product_title, product_price, product_quantity)
    VALUES (?, ?, ?)
    '''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
            conn.commit()

    except sqlite3.Error as e:
        print(e)


def update_product_quantity(db_name, product):
    sql = '''UPDATE products SET product_quantity=? WHERE product_id=?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
            conn.commit()

    except sqlite3.Error as e:
        print(e)


def update_product_price(db_name, product):
    sql = '''UPDATE products SET product_price=? WHERE product_id=?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
            conn.commit()

    except sqlite3.Error as e:
        print(e)


def delete_product(db_name, product_id):
    sql = '''DELETE FROM products WHERE product_id=?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (product_id,))
            conn.commit()

    except sqlite3.Error as e:
        print(e)


def select_product(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print(e)


def select_product_by_parameters(db_name, price_limit, remainder_of_quantity):
    sql = '''SELECT * FROM products WHERE product_price<=? AND product_quantity>=?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (price_limit, remainder_of_quantity))
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print(e)


def select_product_by_title(db_name, product_title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (f'%{product_title}%',))
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print(e)


db_name = '''hw.db'''
create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    product_price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    product_quantity INTEGER NOT NULL DEFAULT 0
)
'''
create_table(db_name, create_products_table)
# insert_product(db_name, ("Cola", 55.99, 10))
# insert_product(db_name, ("Fanta", 60.55, 15))
# insert_product(db_name, ("Sprite", 50, 20))
# insert_product(db_name, ("Pepsi", 55, 10))
# insert_product(db_name, ("Fuse Tea", 64.34, 20))
# insert_product(db_name, ("Nitro", 76.45, 30))
# insert_product(db_name, ("Flesh", 75.65, 20))
# insert_product(db_name, ("Gorilla", 75, 16))
# insert_product(db_name, ("Red Bull", 85.80, 14))
# insert_product(db_name, ("Mojito", 55, 10))
# insert_product(db_name, ("Tan", 65.99, 17))
# insert_product(db_name, ("Aralash", 59.67, 19))
# insert_product(db_name, ("Maksym", 55, 30))
# insert_product(db_name, ("Bozo", 65.98, 30))
# insert_product(db_name, ("Chalap", 55, 10))
# update_product_quantity(db_name, (20, 1))
# update_product_price(db_name, (60, 1))
# delete_product(db_name, 15)
# select_product(db_name)
# select_product_by_parameters(db_name, 70, 15)
# select_product_by_title(db_name, "o")
