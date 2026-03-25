import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
""")

cursor.executemany("INSERT INTO users (name) VALUES (?)", [
    ("Аня",),
    ("Иван",),
    ("Саша",),
    ("Оля",),
    ("Макс",)
])

cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", [
    ("Интерстеллар", "Фантастика"),
    ("Титаник", "Драма"),
    ("Джокер", "Триллер"),
    ("Мстители", "Экшн"),
    ("Гарри Поттер", "Фэнтези")
])

cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", [
    (1, 1, 9),
    (2, 1, 8),
    (3, 2, 10),
    (4, 2, 7),
    (5, 3, 9),
    (1, 3, 8),
    (2, 4, 7),
    (3, 4, 9),
    (4, 5, 10),
    (5, 5, 8)
])

conn.commit()

print("JOIN: пользователь + фильм + оценка")
for row in cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
"""):
    print(row)

print("\nВсе фильмы (даже без отзывов):")
for row in cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
"""):
    print(row)

print("\nАгрегации:")
avg = cursor.execute("SELECT AVG(rating) FROM reviews").fetchone()[0]
max_rating = cursor.execute("SELECT MAX(rating) FROM reviews").fetchone()[0]
min_rating = cursor.execute("SELECT MIN(rating) FROM reviews").fetchone()[0]

print("Средняя оценка:", avg)
print("Максимальная оценка:", max_rating)
print("Минимальная оценка:", min_rating)

conn.close()