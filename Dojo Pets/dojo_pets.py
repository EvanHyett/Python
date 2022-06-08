class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self
        
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5

    def noise(self):
        print(self.sound)
        return self

class Dog(Pet):
    def __init__(self, name, type, tricks, sound):
        super().__init__(name, type, tricks, sound)

beckett = Pet('Beckett', 'Labradoodle', ['Sit', 'Up', 'High-Five'], 'Ruff')


evan_ninja = Ninja('Evan', 'Hyett', ['greenie', 'chewy', 'bone'], ['chicken', 'peanut butter', 'steak'], beckett)
evan_ninja.walk()
evan_ninja.feed()
evan_ninja.bathe()

print(evan_ninja.pet.name)
print(evan_ninja.pet.health)
print(evan_ninja.pet.energy)