lowest = None

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        if lowest is None or number < lowest:
            lowest = number
    except ValueError:
        break

if lowest is not None:
    print("The lowest number entered is:", lowest)
else:
    print("No valid numbers were entered.")