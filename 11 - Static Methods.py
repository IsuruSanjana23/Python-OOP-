class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Janitor"]
        return position in valid_positions

employee1 = Employee("John Doe", "Manager")
print(employee1.get_info())
print(Employee.is_valid_position("Manager"))  # True