numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nNumbers without duplicates:")

for n in numbers:
    if numbers.count(n) == 1:
        print(n)