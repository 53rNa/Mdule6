# БЗадача "Съедобное, несъедобное"

# Родительские классы Animal и Plant с соответствующими атрибутами и методами
class Animal:
    def __init__(self, name):
        self.alive = True                                   # живой
        self.fed = False                                    # накормленный
        self.name = name
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

# Классы-наследники для Animal
class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:         # Если растения съдобные
            self.fed = True
            print(f"{self.name} съел {food.name}.")
        else:
            self.alive = False
            self.fed = False
            print(f"{self.name} не стал есть {food.name}")
class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:         # Если растения съдобные
                self.fed = True
                # self.alive = True
                print(f"{self.name} съел {food.name}.")
        else:
                self.alive = False
                self.fed = False
                print(f"{self.name} не стал есть {food.name}")

# Классы-наследники для Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False  # Цветок несъедобен
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукт съедобен

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
