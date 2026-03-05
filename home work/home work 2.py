import random


# Родительский класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, мой уровень {self.level}.")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье. Теперь здоровье: {self.health}")


# Класс Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


# Класс Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


# Класс Assassin
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


# Создание объектов
warrior = Warrior("Тор", 5, 100, 20, 50)
mage = Mage("Мерлин", 5, 80, 25, 100)
assassin = Assassin("Шэдоу", 5, 90, 30, 80)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

# Мини-игра
print("Выберите героя: Warrior / Mage / Assassin")
choice = input("Ваш выбор: ").lower()

if choice not in heroes:
    print("Неверный выбор героя.")
else:
    player = heroes[choice]

    opponent = random.choice(list(heroes.values()))

    print(f"\nВы выбрали: {player.__class__.__name__}")
    print(f"Противник: {opponent.__class__.__name__}\n")

    player.attack()
    opponent.attack()

    player_type = player.__class__.__name__
    opponent_type = opponent.__class__.__name__

    if player_type == opponent_type:
        print("Ничья!")
    elif (
        (player_type == "Warrior" and opponent_type == "Assassin") or
        (player_type == "Assassin" and opponent_type == "Mage") or
        (player_type == "Mage" and opponent_type == "Warrior")
    ):
        print(f"{player_type} победил!")
    else:
        print(f"{opponent_type} победил!")