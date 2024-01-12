class Payroll:
    # Initialize with all the variables
    def __init__(self, employee_id, employee_first_name, employee_last_name, sales_amt, advanced_pay):
        self.employee_id = employee_id
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name
        self.sales_amt = sales_amt
        self.advanced_pay = advanced_pay

    def calc_pay(self):
        # Find commission based on sales amount
        if self.sales_amt >= 22000:
            commission = 0.18
        elif self.sales_amt >= 18000:
            commission = 0.16
        elif self.sales_amt >= 15000:
            commission = 0.14
        elif self.sales_amt >= 10000:
            commission = 0.12
        else:
            commission = 0.10

        # Calculate pay with previously found commission rate
        pay = self.sales_amt * commission - self.advanced_pay
        return pay

    def display(self):
        # Print all the info
        print(f'Name: {self.employee_first_name} {self.employee_last_name}')
        print(f'ID: {self.employee_id}')
        print(f'Sales Amount: {self.sales_amt}')
        print(f'Advanced Pay: {self.advanced_pay}')
        print(f'Total Pay: {self.calc_pay()}')
