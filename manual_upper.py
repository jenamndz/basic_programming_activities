text = input("Enter string: ")

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
result = ""

for char in text:
    if char in lower:
        index = lower.find(char)
        result += UPPER[index]
    else:
        result += char