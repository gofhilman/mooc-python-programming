# Write your solution here
quantity = int(input("How many: "))
items = []
for i in range(quantity):
    value = int(input(f"Item {i + 1}: "))
    items.append(value)
print(items)
