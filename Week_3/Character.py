char = input("Enter a character: ")

for line in range(1, 10, 2):
    if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        pattern = char * line
        print(pattern)
        