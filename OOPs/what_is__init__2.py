class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      # set brand attribute
        self.model = model      # set model attribute
        self.year = year        # set year attribute


    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


# Create objects (instances)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)

# Use the method
car1.display_info()   # Output: 2020 Toyota Corolla
car2.display_info()   # Output: 2023 Tesla Model 3




'''
 What happened:
__init__ automatically runs when you do car1 = Car(...).
It sets the values of brand, model, and year inside each object.
You can then use those values in other methods (like display_info()).
'''





'''
Output :
2020 Toyota Corolla
2023 Tesla Model 3

'''
