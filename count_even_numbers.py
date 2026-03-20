even = 0

for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    if number % 2 == 0:
        even += 1

print(f"There are {even} even numbers")