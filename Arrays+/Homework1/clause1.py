 ###Homework###
 #Create a list with 10 students grades
 #Print every grade using a loop
 #Calculate the average without using sum()
 #Ask the user for a grade to search for and report its first position
 #Replace every grade below 70 with 70
 #Print the final list and new average

total=0
Grades = [int(input("Enter the grades!:")) for i in range(10)]
for i in Grades:
    print("The grade of the position", Grades.index(i), "is:", i)
for number in Grades:
    total += number 
average=total/ len(Grades)
print(f"The average of the grades is: {average}")
index_grade = int(input("Enter the grade you want to search for!: "))
if index_grade in Grades:
    print(f"The student was found in the list! His grade is: {index_grade}")
else:
    print("The student wasn't found in the list!")
print(Grades)
