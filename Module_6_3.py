import random


class Animal:
    live = True
    sound = None # - звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0] #  - координаты в пространстве
        self.speed = speed #... - скорость передвижения существа (определяется при создании объекта)

    def move(self, dx, dy, dz):
        if dz < 0:
            print(f"It's too deep, i can't dive :(")
            self._cords = [dx, dy, dz]
        else:
            self._cords = list(map(lambda x: x * self.speed, [dx, dy, dz]))
        return self._cords

    def get_cords(self):
        print(f'X:{self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful :)")
        else:
            print(f"Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True # - наличие клюва

    def lay_eggs(self):
        random_eggs = random.randint(1, 4)
        print(f"Here are(is) {random_eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.speed /= 2
        self._cords[2] -= int(abs(dz) * self.speed)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()