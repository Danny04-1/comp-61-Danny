temp=input("Please input the temperature: ")
print('The current Temerature is: ',temp)

weathercondition= input("Please enter: sunny, rainy, or cloudy ")
print("The weather condition is: " + weathercondition)

budget= input("Please enter today's budget: ")
print("Taday's budget is, ", budget)

if(weathercondition=="sunny"):
    if(temp>='75') and (budget>="20"):
        print("Go to the beach!")
    else:
        print("Have a picnic in the park.")

if(weathercondition=="sunny"):
    if(temp>="75") and (budget>= "20"):
        print("Go to the beach!")
    else:
        print("Have a picnic in the park.")

if(weathercondition== "rainy"):
    if(budget>="15"):
        print("Visit a musem.")
    else:
        print("Stay in and watch a movie at home.")

if(weathercondition=="cloudy") or (temp<="60"):
    print("Go to a coffee shop and enjoy a warm drink.")
