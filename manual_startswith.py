text = input("Enter the main string: ")
prefix = input("Enter the ending to check: ")

n = len(prefix)

beginning = text[:n]

if prefix == beginning:
    print("Output: True")
else:
    print("Output: False")
