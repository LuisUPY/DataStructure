 ###Homework###
 #Create a list with 10 students grades
 #Print every grade using a loop
 #Calculate the average without using sum()
 #Ask the user for a grade to search for and report its first position
 #Replace every grade below 70 with 70
 #Print the final list and new average
Grades = [int(input("Enter the grades!:")) for i in range(10)]
for i in Grades:
    print("The grade of the position", Grades.index(i), "is:", i)
index_grade = int(input("Enter the index of the student you want to search for!: "))
print("The grade at that position is:", Grades[index_grade])
new_grade = int(input("Enter the new grade!: "))
new_position = int(input("Enter the position where you want to insert the grade!: "))
Grades.insert(new_position, new_grade)
print("The updated list is:", Grades)