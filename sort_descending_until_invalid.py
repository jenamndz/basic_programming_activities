numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = float (user_input)
        numbers.append(number)
    except ValueError:
        break

if numbers:
    numbers.sort(reverse=True)
    print("\nNumbers from highest to lowest:")
    print(numbers)
else:
    print("No valid numbers were entered.")