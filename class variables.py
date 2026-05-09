class Car:

    total_cars = 0
    company_name = "Isuru"

    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.total_cars += 1

car1 = Car("Ferrari",2020 , "Red" , True)
car2 = Car("Volvo",2020 , "Red" , False)
print(Car.total_cars)