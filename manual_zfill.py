text = input("Enter string: ")
total_length = int(input("Enter total characters desired: "))

while len(text) < total_length:
    text = "0" + text
