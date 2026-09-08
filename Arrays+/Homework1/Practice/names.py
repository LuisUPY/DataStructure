names = ["Alejandro", "Arcadio", "Cristian", "Jaen", "Luis"]
print(names[2: ])
print(names[1:4])
names.remove("Alejandro")
print(names)
names.append(input("Enter a name to add!: "))
print(names)
names.remove(input("Enter a name to remove! (select the position): "))
print(names)
del names[int(input("Enter the index you want to delete!: "))]
print(names)