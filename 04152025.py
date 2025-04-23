#x=-1
#while(True):
#    try:
#        x=3
#        y=3+1
#        x=int(input("Please enter number between 1-2: "))
 #   except:
#        x=1
#        print("something went wrong")
#    finally:
#        x==1 
 #       print("Hello")
#        x=2
#        print("Bye")
    
#print("finish")
#accidentally deleted so this is wrong#

#a=-1
#b="" 
#c=''
#while(True):
#    try:
#        a=int(input("Please enter a int number: "))
#    except:
#        print("looks like you enter the string instead of int")
#    else:
#        print("You entered", a)
#    finally:
#        print("I am gonna run anyway")
#
#    b=input("enter a string: ")
#
#    if (a==1):
#        print("Hello")
#
#    if(b=='lol'):
#        print("haha")
#
#    try:
#        if(a+b==3):
#            print("hihihi")
#    except:
#        print("Looks the type may mismatch or some other error")


#a=-1
#b='abc'
#try:
#    a=int(input("Please enter a int number: "))
#    c=a+b
#except TypeError as e:
#    print("TypeError---------")
#    print(e)
#    c=3
#except Exception as e:
#    print('Exception-----------')
#    print(e)
#    print("Looks like you enter the string instead of int")
#finally:
#    print("this gonna run anyway")
#
#if(c==3):
#    print('hello')
#    print('a=', a)


# on final Exam #

b=2
def test_input():
    global b
    try:
        _a=int(input("please enter a int number: "))
        return _a
    except Exception as e:
        print(e)
    else:
        _a=2
    finally:
        b=3
        print("hello")
        _a=3
        return _a


a=3
a=test_input()
print(a+b)


