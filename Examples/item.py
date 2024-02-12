# Enio Hysa
# 2/7 Practice

class Item:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def set_name(self, str1):
        self.__name = str1

    def set_quantity(self, q):
        self.__quantity = q

    def display(self):
        print(f'Name:{self.__name}\nQuantity: {self.__quantity}')


#inner module testing
if __name__ == '__main__':
    cereal = Item('Smith Cereal', 500)
    cereal.display()
    #not a general Item
    # milk = Item('Organic milk', 1000, )
    book = Item('Python programming', 100)
    book.display()
