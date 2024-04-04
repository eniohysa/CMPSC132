class Node:
    def __init__(self, d=None):
        self.__data = d
        self.next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def __str__(self):
        # only display the data
        return f'{self.__data}'
