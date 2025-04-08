# class Year:

#     def __init__(self, year):
#         self.__year = year

#     @property
#     def year(self):
#         return self.__year

# y = Year(2025)
# print(y.year)


# Написать (из ДЗ) класс "человек",
# 1. Простой случай - имя - property (показать пример)
# 2. Сложный случай - есть дата рожения, возраст - это свойство (property) - показать пример

from datetime import datetime
# class Human:
#     def __init__(self, name, birthday):
#         self.__name = name
#         self.__birthday = birthday
#         self.now = datetime.now()
    
#     @property
#     def age(self):
#         return self.now.year - self.__birthday.year

# human = Human('Chel', datetime(2000,11,22))

# print(f'Возраст = {human.age}')

class MyCalendar:

    def __init__(self, year, month=1, day=1):
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def leap(self):
        # Проверка на високосный год
        return (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0)

    @property
    def year(self):
        return self.__year
    
    @property
    def day(self):
        return self.__day
    
        # Функция, не меняющая поля класса!
    def days_in_month(self, month_number):  # 1..12
        if month_number in [4, 6, 9, 11]:
            # Апрель, Июнь, Сентябрь, Ноябрь
            return 30
        elif month_number == 2:
            if self.leap:
                # Високосный Февраль
                return 29
            # Невисокосный Февраль
            return 28
        return 31

    def set_day(self, new_day):
        if isinstance(new_day, int):
            # Убедились, что перед нами - целое число,
            if 0 < new_day <= self.days_in_month(self.__month):
                # не меньше 1 и не больше числа дней в ЭТОМ месяце
                self.__day = new_day
            else:
                print('Неверный номер дня %i для меяца %i' % (
                    new_day, self.__month))
        else:
            print('Неверно, день должен быть числом, а не %s!' % new_day)
    
    def set_month(self, month_num):
        if 1 <= month_num <=12:
            self.__month = month_num 
        else:
            print('Нет такого месяца')
        
    def __str__(self):
        return f'{self.__day}-{self.__month}-{self.__year}'

mc = MyCalendar(2025, 6, 29)
mc.set_day(2)
mc.set_month(8)
print(mc)

