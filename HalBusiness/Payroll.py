class Payroll:
    # Initialize with all the variables
    def __init__(self, employee_id, employee_first_name, employee_last_name, sales_amt, advanced_pay):
        self.__employee_id = employee_id
        self.__employee_first_name = employee_first_name
        self.__employee_last_name = employee_last_name
        self.__sales_amt = sales_amt
        self.__advanced_pay = advanced_pay

    # Setter functions
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_employee_first_name(self, employee_first_name):
        self.__employee_first_name = employee_first_name

    def set_employee_last_name(self, employee_last_name):
        self.__employee_last_name = employee_last_name

    def set_sales_amt(self, sales_amt):
        self.__sales_amt = sales_amt

    def set_advanced_pay(self, advanced_pay):
        self.__advanced_pay = advanced_pay

    # Getter functions
    def get_employee_id(self):
        return self.__employee_id

    def get_employee_first_name(self):
        return self.__employee_first_name

    def get_employee_last_name(self):
        return self.__employee_last_name

    def get_sales_amt(self):
        return self.__sales_amt

    def get_advanced_pay(self):
        return self.__advanced_pay

    # Calculate pay
    def calc_pay(self):
        # Find commission based on sales amount
        if self.__sales_amt >= 22000:
            commission = 0.18
        elif self.__sales_amt >= 18000:
            commission = 0.16
        elif self.__sales_amt >= 15000:
            commission = 0.14
        elif self.__sales_amt >= 10000:
            commission = 0.12
        else:
            commission = 0.10

        # Calculate pay with previously found commission rate
        pay = self.__sales_amt * commission - self.__advanced_pay
        return pay

    # Print all the info
    def display(self):
        # Print all the info
        print(f'Name: {self.__employee_first_name} {self.__employee_last_name}')
        print(f'ID: {self.__employee_id}')
        print(f'Sales Amount: ${self.__sales_amt}')
        print(f'Advanced Pay: ${self.__advanced_pay}')
        print(f'Total Pay: ${self.calc_pay()}\n')
