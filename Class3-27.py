#class Person:
#    pass
#a_list=['a',True,1,Person()]
#a_list= [1,2,3]
#b_list=[4,5,6,]
#c_list=[a_list,b_list] #2d list
#f_list=[a_list, b_list] #3d list
#print(c_list[0])  #1d list-> list
#print(c_list[0][1])# get number 2 from a_list
#if (len(c_list[1])>4):
#    print(c_list[1][4])
#else:
#    print("index 4")
#
#
#
#d_list=[[1,2,3],
#        [4,5,6]]
#print(c_list[0][0])
class Person:
    def __init__(self, _first_name, _last_name, _daily_salary):
        self.money = 0
        self.first_name = _first_name
        self.last_name = _last_name
        self.daily_salary = _daily_salary
    
    def work(self, _day):
        salary = self.daily_salary * _day
        self.money = self.money + salary

    def work_a_mont(self):
        salary=self.daily_salary * 30
        

shawn = Person("shawn", "lin", 10)
ben = Person("ben", "ben", 20)
breana=Person("breana",'navarro', 19)
marq=Person("marq", 'marv',16)

person_list=[shawn,ben,breana,marq]
rich_person= None
most_daily_salary=0
for person in person_list:
    if(person.daily_salary > most_daily_salary):
        rich_person=person
        most_daily_salary=rich_person.daily_salary

print(rich_person.first_name, rich_person.last_name)



shawn.work(30)
ben.work(15)

if(shawn.money > ben.money):
    print("Shawn has more money")
else:
    print("Ben has more money")

