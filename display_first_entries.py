numbers = []

for i in range (10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

seen = []

print("Numbers (duplicates shown only once):")
for num in numbers:
    if num not in seen:
        print(num)
        seen.append(num)