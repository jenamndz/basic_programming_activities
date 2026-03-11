total_sum = 0

print("Enter 10 numbers")

for i in range(1,11):
    number = int(input(f"Enter number {i}: "))

    total_sum += number

print(f"\nThe sum of all 10 numbers is: {total_sum}")