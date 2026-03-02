# Создание класса Hero
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    # 1️⃣ Приветствие
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    # 2️⃣ Атака
    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1
        print(f"Сила уменьшилась. Текущая сила: {self.strength}")

    # 3️⃣ Отдых
    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1
        print(f"Здоровье увеличилось. Текущее здоровье: {self.health}")


# 🔹 Создание объектов
hero1 = Hero("Артур", 5, 10, 7)
hero2 = Hero("Луна", 3, 8, 6)

# 🔹 Проверка методов первого героя
hero1.greet()
hero1.attack()
hero1.rest()

print("------------------")

# 🔹 Проверка методов второго героя
hero2.greet()
hero2.attack()
hero2.rest()