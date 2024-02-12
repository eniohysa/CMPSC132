from item import Item


class Produce(Item):
    def __init__(self, name, quantity, expiration=' '):
        Item.__init__(self, name, quantity)
        # Item(name, quantity)
        self.__expirationDate = expiration

    def set_expiration(self, expiration):
        self.__expirationDate = expiration

    def get_expiration(self):
        return self.__expirationDate

    #override the display method
    def display(self):
        Item.display(self)   #call the superclass's init()
        print('Expiration Date: ', self.__expirationDate)


if __name__ == '__main__':
    milk = Produce('Organic milk', 100, '10/1/2023')
    milk.display()
    apple = Produce('Fuji', 200)
    apple.display()
