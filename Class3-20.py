counter=10

def count_down(count):
    global counter
    if count==0:
        print('Go!')
    else:
        print(count)
        count_down(count-1)

def count_up(count):
    global counter
    if count==10:
        counter=count
        print('Go!')
    else:
        print(count)
        count_up(count+1)
        

count_down(counter)

count_up(counter)
