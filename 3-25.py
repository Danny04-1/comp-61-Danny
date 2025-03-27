#line = ""
#for i in range(5):
#    for j in range(5):
#       line += str(i) + str(j)
#    print(line)
#    line = ""
#
#a_list = [0, 1, 2, 3, 4]
#print(a_list)
#a_list[2] = 10
#print(a_list[2])
#
#a_list = [0, 1, 2, 3, 4]
#two_d_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#
#print(two_d_list)

#-----------------------------------------------------------------------------


#line = ""
#for i in range(3):
#    for j in range(3):
#        line += str(i) + str(j) + " "
#    print(line)
#    line = ""
#
#two_d_lists = []
#line = []
#for i in range(3):
#    for j in range(3):
#        if (i == j):
#            line.append("*")
#        else:
#            line.append(" ")

#---------------------------------

import random 

two_d_list = []
line= []
for i in range(3):
    for j in range(3):
        for j in range(3):
            line.append(random.randint(0,1))
        two_d_list.append(line)
        line = []

print(two_d_list)

input_x=int(input("input x position: "))
input_y=int(input("Input y position: "))

if(two_d_list(input_x)(input_y)==1):
    print("you lose")

else:
    print("Keep going")


