lowest = None

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        if lowest is None or number < lowest:
            lowest = number
    except ValueError:
        break
