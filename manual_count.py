text = input("Enter the string: ")
target = input("Enter character to count: ")

counter = 0
for char in text:
    if char == target:
        counter += 1
