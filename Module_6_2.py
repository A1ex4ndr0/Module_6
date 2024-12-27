class Vehicle:
    __COLOR_VARIANTS = ["White", "Black", "Aquamarine", "Red", "Green"]

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f'Модель: {self.__model}', end = ', ')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}', end = ', ')

    def get_color(self):
        print(f'Цвет: {self.__color}', end = ', ')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        flag = False
        for i in self.__COLOR_VARIANTS:
            if new_color.upper() == i.upper():
                flag = True
        if flag:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'Blue')

vehicle1.print_info()

vehicle1.set_color('Gray')
vehicle1.set_color('Aquamarine')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()