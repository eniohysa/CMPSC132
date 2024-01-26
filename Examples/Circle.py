# Name: Enio Hysa
# Course: CMPSC132
# File Name: Circle.py
# Date: 1/24/24

import math


class Circle:
    def __init__(self):
        # Constructor
        self.__radius = 0.0  # Private data

    def set_radius(self, r):
        self.__radius = r

    def get_radius(self):
        return self.__radius

    def calc_area(self):
        area = self.__radius ** 2 * math.pi
        return area

    def calc_perimeter(self):
        perimeter = self.__radius * 2 * math.pi
        return perimeter

    def display(self):
        print(f'The circle with radius = {self.__radius:.2f}\n'
              f'area = {self.calc_area():.2f}\n'
              f'perimeter = {self.calc_perimeter():.2f}')


if __name__ == '__main__':
    # Circle 1, radius = 5
    circle1 = Circle()
    circle1.set_radius(5)
    circle1.display()
