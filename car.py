# Машина:
# Должна быть возможность прочитать и записать марку,
# год выпуска, скорость, расстояние

# Посчитать (в шутку), за какое время
# машина могла бы пройти это расстояние с указанной скоростью
# Сделать возможность УКАЗАТЬ время, а на самом деле изменить расстояние

class Car:
    def __init__(self, brand, year, speed, distance):
        self.__brand = brand
        self.__year = year
        self.__speed = speed
        self.__distance = distance

    @property
    def brand(self):
        return self.__brand
    
    @property
    def year(self):
        return self.__year
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def distance(self):
        return self.__distance

    @brand.setter
    def brand (self, brand):
        self.brand = brand

    @year.setter
    def year (self, year):
        self.year = year

    @speed.setter
    def speed (self, speed):
        self.speed = speed

    @distance.setter
    def distance(self, distance):
        self.distance = distance

    def countTime (self):
        return f'Машина пройдёт {self.distance} км за {self.distance / self.speed} часов'

    def countDistance (self, time):
        return f'За {time} часов машина проедет {time * self.speed} км'
    
    def __str__(self):
        return f'Машина марки {car.brand}, выпущена в {car.year} году, скорость - {car.speed} км/ч, расстояние - {car.distance}'
    
    

car = Car('BMW', 2012, 100, 500)

print(car)

print(car.countTime())

print(car.countDistance(7))


    


    