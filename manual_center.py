text = input("Enter string: ")
total_length = int(input("Enter total characters: "))

while len(text) < total_length:
    text = " " + text

    if len(text) == total_length:
        break

    text = text + " "