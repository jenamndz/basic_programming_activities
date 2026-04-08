text = input("Enter string: ")
prefix = input("Enter prefix to remove: ")

if text[:len(prefix)] == prefix:
    result = text[len(prefix):]
else:
    result = text

print(f"Output: {result}")