import random

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}")
        enemy.health -= 20
        print(f"У {enemy.name} осталось {enemy.health} очков здоровья\n")

# Создаем двух юнитов
warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while warrior1.health > 0 and warrior2.health > 0:
    attacker = random.choice([warrior1, warrior2])
    enemy = warrior2 if attacker == warrior1 else warrior1
    attacker.attack(enemy)

if warrior1.health <= 0 and warrior2.health <= 0:
    print("Ничья!")
elif warrior1.health > 0:
    print(f"{warrior1.name} одержал победу!")
else:
    print(f"{warrior2.name} одержал победу!")