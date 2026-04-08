text = input("Enter a statement with spaces in the beginning: ")

while text.startswith(" "):
    text = text[1:]

print(f"Output: '{text}'")