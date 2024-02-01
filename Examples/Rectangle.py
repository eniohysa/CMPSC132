class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def calc_area(self):
        return self.__length * self.__width

    def calc_perimeter(self):
        return 2 * self.__length + 2 * self.__width

    def display(self):
        print('Length: ', self.get_length())
        print('Width: ', self.get_width())
        print('Perimeter: ', self.calc_perimeter())
        print('Area: ', self.calc_area())
