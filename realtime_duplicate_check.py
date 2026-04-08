numbers = []

while True:
    user_input = input("Enter a number (or any non-number to stop): ")
    if not user_input.isdigit():
        print("Invalid input. Stopping program.")
        break

    num = int(user_input)

    if num in numbers:
        print(f"{num} - Duplicate")
    else:
        print(f"{num} - Unique")
        numbers.append(num)