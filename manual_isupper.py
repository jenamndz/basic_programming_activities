text = input("Enter string: ")
is_all_upper = True

for char in text:
    if 'a' <= char <= 'z':
        is_all_upper = False
        break

print(f"Output: {is_all_upper}")