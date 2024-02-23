from Mother import Human
from date import Date


class Child(Human):
    def __init__(self, name, bday, school=''):
        Human.__init__(self, name, bday)
        self.__school = school

    def get_school(self):
        return self.__school

    def display(self):
        print(f'Student name: {self.__name}')
        print(f'DOB: {self.__dob}')
        print(f'School: {self.__school}')


if __name__ == '__main__':
    name = input('Enter name: ')

    month = int(input('Enter the month: '))
    day = int(input('Enter the day: '))
    year = int(input('Enter the year: '))
    dob = Date(month, day, year)

    school = input('Enter school name: ')

    child1 = Child(name, dob, school)
    child1.display()
