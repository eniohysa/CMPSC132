# Name: Enio Hysa
# Course: CMPSC132
# File Name: Circle.py
# Date: 1/24/24

import math


class Circle:
    def __init__(self, r):
        # Constructor
        self.__radius = r  # Private data

    def __str__(self):
        return f'Circle rad={self.__radius:.2f}\narea={self.calc_area():.2f}\nperimeter={self.calc_perimeter():.2f}\n'

    def get_radius(self):
        return self.__radius

    def set_radius(self, r):
        self.__radius = r

    def calc_area(self):
        area = self.__radius ** 2 * math.pi
        return area

    def calc_perimeter(self):
        perimeter = self.__radius * 2 * math.pi
        return perimeter

    def display(self):
        print(f'The circle with radius = {self.__radius:.2f}\n'
              f'area = {self.calc_area():.2f}\n'
              f'perimeter = {self.calc_perimeter():.2f}\n')


if __name__ == '__main__':
    # Circle 1, radius = 5
    circle1 = Circle(r=5)
    circle1.display()

    circle2 = Circle(r=10)
    circle2.display()

    circle3 = Circle(7)
    circle3.set_radius(13)
    circle3.display()
