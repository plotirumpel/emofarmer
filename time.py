class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def show(self):
        print(f'{self.hours}:{self.minutes}')

    def isDay(self):
        check = False
        if 12 <= self.hours < 17:
            check = True
            self.timeofday = 'день'
        print(check)

    def isMorning(self):
        check = False
        if 5 <= self.hours < 12:
            check = True
            self.timeofday = 'утро'
        print(check)

    def isEvening(self):
        check = False
        if 17 <= self.hours <= 23:
            check = True
            self.timeofday = 'вечер'
        print(check)

    def isNight(self):
        check = False
        if 0 <= self.hours < 5:
            check = True
            self.timeofday = 'ночь'
        print(check)

    def say_hello(self):
        if self.timeofday == 'утро':
            print('Доброе утро')
        if self.timeofday == 'день' or self.timeofday == 'вечер':
            print(f"Добрый {self.timeofday}")
        if self.timeofday == 'ночь':
            print("Доброй ночи")

    def add(self, add):
        added = self.minutes + add
        self.hours += added // 60
        self.minutes = added % 60
        self.show()
import math
print(math.gcd (10,20))
print(math.gcd (57,2))