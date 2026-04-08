highest = None

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        if highest is None or number > highest:
            highest = number
    except ValueError:
        break