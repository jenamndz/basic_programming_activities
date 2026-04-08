numbers = []

print("Enter numbers (Enter any letter or symbol to stop):")

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

if numbers:
    numbers.sort()
    print("\nNumbers from lowest to highest:")
    print(numbers)
else:
    print("No valid numbers were entered.")