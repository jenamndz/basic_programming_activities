numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

if numbers:
    average = sum(numbers) / len(numbers)
    print("The average number is:", average)
else:
    print("No numbers entered")