numbers = []

for i in range (10):
    num = int(input(f"Enter the number {i+1} : "))
    numbers.append(num)

duplicate_numbers = []
seen_as_duplicate = []

for n in numbers:
    if numbers.count(n) > 1 and n not in seen_as_duplicate:
        duplicate_numbers.append(n)

