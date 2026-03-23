import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")
conn.commit()


# CREATE — добавление товара
def create_product(name, price, quantity):
    cursor.execute("""
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    """, (name, price, quantity))
    conn.commit()


# READ — получение всех товаров
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)


# UPDATE — обновление цены товара по id
def update_product(product_id, price):
    cursor.execute("""
    UPDATE products
    SET price = ?
    WHERE id = ?
    """, (price, product_id))
    conn.commit()


# DELETE — удаление товара по id
def delete_product(product_id):
    cursor.execute("""
    DELETE FROM products
    WHERE id = ?
    """, (product_id,))
    conn.commit()


# Пример использования
if __name__ == "__main__":
    # Добавление товаров
    create_product("Apple", 1.5, 100)
    create_product("Banana", 0.8, 150)

    # Чтение
    print("Список товаров:")
    read_products()

    # Обновление
    update_product(1, 2.0)

    print("\nПосле обновления:")
    read_products()

    # Удаление
    delete_product(2)

    print("\nПосле удаления:")
    read_products()

    # Закрытие соединения
    conn.close()