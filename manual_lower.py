text = input("Enter string: ")

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
result = ""

for char in text:
    if char in UPPER:
        index = UPPER.find(char)
        result += lower[index]
    else:
        result += char