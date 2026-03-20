numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

answer = numbers[0]

for i in range(1,10):
    answer -= numbers[i]

print(f"\nThe answer is: {answer}")