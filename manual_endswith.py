text = input("Enter the main string: ")
suffix = input("Enter the ending to check: ")

n = len(suffix)

end_part = text[-n:]

if end_part == suffix:
    print("Output: True")
else:
    print("Output: False")