class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"{self.make} {self.model} {self.year}"

class Owner:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.cars_owned = []

    def purchase_car(self, Car):
        self.cars_owned.append(Car) 
        print(f"{self.name} just purchased {Car.get_car_info()}")

    def show_owned_cars(self): 
        if len(self.cars_owned) > 0:
            print(f"{self.name} owns these cars: ")
            for Car in self.cars_owned:
                print(f"{Car.get_car_info()}")
        else:
            print(f"{self.name} doesnt own any cars.")



def Main():
    Owner1 = Owner("Danny", 20)
    Owner2 = Owner("Breana", 19)
    Owner3 = Owner("Marv", 41)

    car1 = Car("Ram", "2500", 2009)
    car2 =Car("Chevy", "Silverado", 2017)
    car3 = Car("Chevy", "Suburban", 2022)
    car4= Car("Audi", "Q5", 2022)
    car5= Car("Ford", "Explorer", 2004)

    Owner1.purchase_car(car1)
    Owner2.purchase_car(car3)
    Owner3.purchase_car(car2)
    Owner2.purchase_car(car5)
    Owner3.purchase_car(car4)

    print("Car ownership Summary")

    Owner1.show_owned_cars()
    Owner2.show_owned_cars()
    Owner3.show_owned_cars()
Main()

