numbers = []

for i in range (10):
    num = int(input(f"Enter the number {i+1} : "))
    numbers.append(num)

duplicate_numbers = []
seen_as_duplicate = []

print("\nNumbers that have duplicates:")

for n in numbers:
    if numbers.count(n) > 1 and n not in seen_as_duplicate:
        print(n)
        seen_as_duplicate.append(n)
        
if not seen_as_duplicate:
    print("No duplicates found.")