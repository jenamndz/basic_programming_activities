odd = 0

print("Enter 10 numbers")

for i in range(1,11):
    number = int(input(f"Enter number {i}: "))

    if number % 2 == 0:
        odd += 1