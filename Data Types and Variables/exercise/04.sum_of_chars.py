number_of_lines = int(input())
sum_chars = 0
for letter in range(0, number_of_lines):
    letters = input()
    sum_chars += ord(letters)
print(f"The sum equals: {sum_chars}")