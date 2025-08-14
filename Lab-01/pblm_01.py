# Find the smallest number in a list using a loop
number = int(input("Enter the number of value in list : "))

list = [2,3,5,3,5,1,6]

min = list[0]
for i in range(0,7) :
    if min > list[i] :
        min = list[i]

print("The small number is : " + str(min))