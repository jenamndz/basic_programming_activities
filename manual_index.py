text = input("Enter string: ")
target = input("Enter character to find: ")

position = -1

for i in range(len(text)):
    if text[i] == target:
        position = i
        break
