text = input("Enter string: ")
suffix = input("Enter suffix to remove: ")

n = len(suffix)

if text[-n:] == suffix:
    result = text[:-n]
else:
    result = text