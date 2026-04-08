text = input("Enter string: ")
is_all_lower = True

for char in text:
    if 'A' <= char <= 'Z':
        is_all_lower = False
        break

print(f"Output: {is_all_lower}")
