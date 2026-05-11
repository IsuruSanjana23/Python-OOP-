class Company:
    class Employee:
        def __init__(self,name,position):
            self.name = name
            self.position = position
        def get_details(self):
            return f"Name: {self.name}\nPosition: {self.position}"

    def __init__(self,company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employees.append(new_employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee.get_details())

company = Company("Pizza Hut")
company.add_employee("John Doe","Manager")
company.add_employee("Jane Smith","Chef")

company.display_employees()