numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break
