from Human import Human


class Mother(Human):
    def __init__(self, name, bday, children=[]):
        Human.__init__(self, name, bday)
        self.__children = children

    def add_child(self, child):
        self.__children.append(child)

    def display(self):
        print(f'name: {self.__name}, bday: {self.__bday}, children: {self.__children}')