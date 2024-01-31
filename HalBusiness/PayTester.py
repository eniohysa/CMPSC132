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
    employee1.set_sales_amt(10000)
    employee1.set_advanced_pay(1000)
    print(f"Updated sales: ${employee1.get_sales_amt()}\n"
          f"Updated advanced pay: ${employee1.get_advanced_pay()}\n"
          f"Updated pay: ${employee1.calc_pay()}\n")

    employee2 = Payroll.Payroll(1101, "John", "Doe", 14500, 200)
    employee2.display()
    employee2.set_employee_id(3690)
    employee2.set_employee_first_name("Jane")
    employee2.set_employee_last_name("Smith")
    print(f"Updated employee ID: {employee2.get_employee_id()}\n"
          f"Updated employee first name: {employee2.get_employee_first_name()}\n"
          f"Updated employee last_name: {employee2.get_employee_last_name()}\n")


if __name__ == '__main__':
    main()

'''Testing Data:
Name: Enio Hysa
ID: 1234
Sales Amount: $25000
Advanced Pay: $0    
Total Pay: $4500.0

Updated sales: $10000
Updated advanced pay: $1000
Updated pay: $200.0

Name: John Doe
ID: 1101
Sales Amount: $14500
Advanced Pay: $200
Total Pay: $1540.0

Updated employee ID: 3690
Updated employee first name: Jane
Updated employee last_name: Smith

'''
