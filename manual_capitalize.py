text = input("Enter string: ")

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
result = ""

n = len(text)

for char in text [0]:
    if char in lower:
        index = lower.find(char)
        result += UPPER[index]
    else:
        result += char

for char in text [1:]:
    if char in UPPER:
        index = UPPER.find(char)
        result += lower[index]
    else:
        result += char

print(f"Output: {result}")