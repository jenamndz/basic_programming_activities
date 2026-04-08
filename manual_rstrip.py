text = input("Enter string with trailing spaces: ")

while text.endswith(" "):
    text = text[:-1]

print(f"Output: '{text}'")