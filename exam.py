import sqlite3


def create_tables(db_name):
    create_categories_table = '''
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150) NOT NULL
    )
    '''

    create_products_table = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(250) NOT NULL,
        category_code VARCHAR(2),
        unit_price FLOAT NOT NULL,
        stock_quantity INTEGER NOT NULL,
        store_id INTEGER,
        FOREIGN KEY(category_code) REFERENCES categories(code),
        FOREIGN KEY(store_id) REFERENCES stores(store_id)
    )
    '''

    create_stores_table = '''
    CREATE TABLE IF NOT EXISTS stores (
        store_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100) NOT NULL
    )
    '''

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_categories_table)
            cursor.execute(create_products_table)
            cursor.execute(create_stores_table)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_category(db_name, category):
    sql = '''INSERT INTO categories (code, title) VALUES (?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, category)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_product(db_name, product):
    sql = '''INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) 
             VALUES (?, ?, ?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_store(db_name, store):
    sql = '''INSERT INTO stores (title) VALUES (?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, store)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


db_name = 'exam.db'


# create_tables(db_name)


# insert_category(db_name, ('FD', 'Food products'))
# insert_category(db_name, ('EL', 'Electronics'))
#
# insert_store(db_name, ('Asia',))
# insert_store(db_name, ('Globus',))
# insert_store(db_name, ('Spar',))
#
# insert_product(db_name, ('Chocolate', 'FD', 10.5, 129, 1))
# insert_product(db_name, ('Milk', 'FD', 2.5, 200, 1))
# insert_product(db_name, ('TV', 'EL', 500.0, 10, 2))
# insert_product(db_name, ('Laptop', 'EL', 1200.0, 5, 3))
# insert_product(db_name, ('Bread', 'FD', 1.2, 150, 1))
# insert_product(db_name, ('Cheese', 'FD', 5.0, 80, 2))
# insert_product(db_name, ('Smartphone', 'EL', 800.0, 20, 3))
# insert_product(db_name, ('Headphones', 'EL', 100.0, 50, 2))
# insert_product(db_name, ('Yogurt', 'FD', 1.0, 300, 1))

def display_stores(db_name):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT store_id, title FROM stores")
            stores = cursor.fetchall()
            for store in stores:
                print(f"{store[0]}. {store[1]}")
    except sqlite3.Error as e:
        print(e)


def display_products_by_store(db_name, store_id):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.title, c.title, p.unit_price, p.stock_quantity
                FROM products p
                JOIN categories c ON p.category_code = c.code
                WHERE p.store_id = ?
            ''', (store_id,))
            products = cursor.fetchall()
            for product in products:
                print(f"Название продукта: {product[0]}")
                print(f"Категория: {product[1]}")
                print(f"Цена: {product[2]}")
                print(f"Количество на складе: {product[3]}")
                print("-------------------")
    except sqlite3.Error as e:
        print(e)


def main():
    db_name = 'exam.db'
    while True:
        print(
            "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
        display_stores(db_name)
        store_id = input("Введите id магазина: ")
        if store_id == '0':
            break
        try:
            store_id = int(store_id)
            display_products_by_store(db_name, store_id)
        except ValueError:
            print("Пожалуйста, введите корректный id магазина.")


if __name__ == "__main__":
    main()
