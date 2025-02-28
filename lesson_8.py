import sqlite3


def create_table_countries(db_name, create_table_sql1):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql1)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_table_cities(db_name, create_table_sql2):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql2)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_table_students(db_name, create_table_sql3):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql3)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_country(db_name, country):
    sql = '''INSERT INTO countries
    (country_title)
    VALUES (?)
    '''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, country)
            conn.commit()

    except sqlite3.Error as e:
        print(e)


def insert_city(db_name, city):
    sql = '''INSERT INTO cities
    (city_title, city_area, country_id)
    VALUES (?, ?, ?)
    '''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, city)
            conn.commit()

    except sqlite3.Error as e:
        print(e)


def insert_student(db_name, student):
    sql = '''INSERT INTO students
    (first_name, last_name, city_id)
    VALUES (?, ?, ?)
    '''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, student)
            conn.commit()

    except sqlite3.Error as e:
        print(e)


def connect_db(db_name):
    return sqlite3.connect(db_name)


def get_cities(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT city_id, city_title FROM cities")
    return cursor.fetchall()


def get_students_by_city(conn, city_id):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT 
        students.first_name, 
        students.last_name, 
        countries.country_title AS country, 
        cities.city_title AS city, 
        cities.city_area 
    FROM students 
    JOIN cities ON students.city_id = cities.city_id 
    JOIN countries ON cities.country_id = countries.country_id 
    WHERE cities.city_id = ?;
    ''', (city_id,))
    return cursor.fetchall()


def main():
    db_name = "hw.db"
    conn = connect_db(db_name)

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    cities = get_cities(conn)
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    while True:
        try:
            city_id = int(input("Введите id города: "))
            if city_id == 0:
                print("Программа завершена.")
                break

            students = get_students_by_city(conn, city_id)
            if students:
                print("\nСписок учеников:")
                for student in students:
                    print(
                        f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]} км²")
            else:
                print("Ученики в этом городе не найдены.")
        except ValueError:
            print("Ошибка: Введите корректный id города (число).")
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")

    conn.close()


if __name__ == "__main__":
    main()

db_name = '''hw.db'''
create_countries_table = '''
CREATE TABLE IF NOT EXISTS countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_title VARCHAR(200) NOT NULL
)
'''
create_cities_table = '''
CREATE TABLE IF NOT EXISTS cities (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_title VARCHAR(200) NOT NULL,
    city_area FLOAT NOT NULL DEFAULT 0.0,
    country_id INTEGER,
    FOREIGN KEY(country_id) REFERENCES countries(country_id)
)
'''
create_students_table = '''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    city_id INTEGER,
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
)
'''
# create_table_countries(db_name, create_countries_table)
# create_table_cities(db_name, create_cities_table)
# create_table_students(db_name, create_students_table)
# insert_country(db_name, "Kyrgyzstan")
# insert_country(db_name, "Germany")
# insert_country(db_name, "China")
# insert_city(db_name, ('Bishkek', 127, 1))
# insert_city(db_name, ('Osh', 182, 1))
# insert_city(db_name, ('Berlin', 891.8, 2))
# insert_city(db_name, ('Munich', 310.4, 2))
# insert_city(db_name, ('Beijing', 16410.5, 3))
# insert_city(db_name, ('Shanghai', 6340.5, 3))
# insert_city(db_name, ('Guangzhou', 7434.4, 3))
# insert_student(db_name, ("Argen", "Beishebaev", 1))
# insert_student(db_name, ("Enir", "Taalaev", 1))
# insert_student(db_name, ("Astra", "Tagaibekova", 3))
# insert_student(db_name, ("Joomart", "Kaliev", 5))
# insert_student(db_name, ("Alex", "Titov", 2))
# insert_student(db_name, ("Atai", "Ashiraliev", 4))
# insert_student(db_name, ("Kanybek", "Abilesov", 3))
# insert_student(db_name, ("Max", "Beyshekeev", 2))
# insert_student(db_name, ("Daniil", "Getman", 3))
# insert_student(db_name, ("Bakai", "Ruslanov", 6))
# insert_student(db_name, ("Dastan", "Eldiyarov", 6))
# insert_student(db_name, ("Kostya", "Suharev", 1))
# insert_student(db_name, ("Aelita", "Mirlanova", 3))
# insert_student(db_name, ("Danat", "Shayliev", 7))
# insert_student(db_name, ("Ahmet", "Musaev", 7))
