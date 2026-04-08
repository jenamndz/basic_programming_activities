text = input("Enter string: ")
target = input("Enter character to find: ")

position = -1

for i in range(len(text)):
    if text[i] == target:
        position = i
        break

if position != -1:
    print(f"Output: {position}")
else:
    print("Character not found.")