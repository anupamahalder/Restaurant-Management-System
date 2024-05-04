from Menu_Class import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] # database
        self.menu = Menu() # Object of Menu to access all of its properties and methods

    def add_employee(self, employee):
        # store the employee object to our database 
        self.employees.append(employee)
        print(f"{employee.name} is added as an Employee successfully!\n")
    
    def view_employee(self):
        if len(self.employees) == 0:
            print("No employee has added yet!")
            return
        print("\nEmployee list!!\n")
        print(f"Name\tEmail\tPhone\tAddress")
        print("--------------------------------------------------")
        for emp in self.employees:
            print(f"{emp.name}\t{emp.email}\t{emp.phone}\t{emp.address}")
        print()
