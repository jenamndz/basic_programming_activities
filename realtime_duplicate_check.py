numbers = []

while True:
    user_input = input("Enter a number (or any non-number to stop): ")
    if not user_input.isdigit():
        print("Invalid input. Stopping program.")
        break
