numbers = []

print("Enter numbers (Type 'stop' or any letter to end):")

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break


if numbers:
    most_frequent = max(set(numbers), key=numbers.count)

    occurrence = numbers.count(most_frequent)


    print(f"\nThe number with the most duplicates is: {most_frequent}")
    print(f"It appeared {occurrence} times.")
else:
    print("No numbers were entered.")