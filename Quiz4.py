class Person: 
    def __init__(self, first_name, last_name, daily_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.daily_salary = daily_salary
        self.money = 0

    def work(self, days):
        salary = days * self.daily_salary
        self.money += salary  


Shawn = Person("Shawn", "Lin", 10)
Ben = Person("Ben", "Ben", 20)

Shawn.work(30)
Ben.work(15)

print(f"Shawn has: {Shawn.money} dollars.")
print(f"Ben has: {Ben.money} dollars.")

print("Shawn and Ben have the same amount of money.")

