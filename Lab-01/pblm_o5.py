# Write a python program to calculate a student's grade based on their marks.
# the program should:
# Take the student's mark (0-100) as input.
# Use conditional statements to determine the grade according to the following rules :
#     a. 90-100: Grade A
#     b. 80-89: Grade B
#     c. 70-79: Grade C
#     d. 60-69: Grade D
#     e. Below 69: Grade F
# print the grade.

mark = int(input("Enter marks(0-100): "))

if 90 <= mark and mark <= 100:
    print("Grade is : A")
elif 80 <= mark and mark <= 89:
    print("Grade is : B")
elif 70 <= mark and mark <= 79:
    print("Grade is : C")
elif 60 <= mark and mark <= 69:
    print("Grade is : D")
else:
    print("Grade is : F")
