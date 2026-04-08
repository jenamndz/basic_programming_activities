text = input("Enter string: ")
target = input("Enter character to find from the end: ")

position = -1

for i in range(len(text) - 1, -1, -1):
    if text[i] == target:
        position = i
        break
