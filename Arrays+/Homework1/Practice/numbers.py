numbers = [i for i in range(int(input("Enter the first number: ")), int(input("Enter the last number: "))+1)]
print(numbers)
del numbers[int(input("Enter the index'es you want to delete!: "))]
print(numbers)
numbers.append(int(input("Enter a number to add!: ")))
print(numbers)
while 10 in numbers:
    numbers.remove(10)
print(numbers)
