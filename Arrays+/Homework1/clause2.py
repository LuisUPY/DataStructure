Inventory = ["Keyboard", "Mouse", "Monitor", "Headset"]
for i in range(len(Inventory)):
    print(i, "-", Inventory[i])
new_product = input("Enter the new product!: ")
new_position = int(input("Enter the position where you want to insert the product!: "))
Inventory.insert(new_position, new_product)
print("The updated inventory is:", Inventory)
remove_product = input("Enter the product you want to remove!: ")
if remove_product in Inventory:
    Inventory.remove(remove_product)
    print("The product was removed successfully!")
else:
    print("The product wasn't found in the inventory!")
print("The final inventory is:", Inventory)
