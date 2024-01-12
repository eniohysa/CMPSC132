# Name: Enio Hysa
# Course: CMPSC132
# File Name: PayTester.py
# Date: 1/11/24
#
# Short Description: Calculate payroll of Hal's Employees
import Payroll


def main():
    employee1 = Payroll.Payroll(1234, "Enio", "Hysa", 25000, 0)
    employee1.display()


if __name__ == '__main__':
    main()
