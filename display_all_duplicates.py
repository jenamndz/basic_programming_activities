numbers = []

for i in range (10):
    num = int(input(f"Enter the number {i+1} : "))
    numbers.append(num)

duplicate_numbers = []

for n in numbers:
    if numbers.count(n) > 1:
        duplicate_numbers.append(n)

