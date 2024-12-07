class Vehicle:
    __COLOR_VARIANTS = ["Белый", "Чёрный", "Морская волна", "Красный", "Беж"]

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
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

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'Синий')

vehicle1.print_info()

vehicle1.set_color('Серый')
vehicle1.set_color('Морская волна')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()