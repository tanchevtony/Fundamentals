# count_balanced = 0
# count_unbalanced = 0
# number_of_lines = int(input())
# for symb in range(number_of_lines):
#     symbol = input()
#     if symbol == "(":
#         count_unbalanced += 1
#     elif symbol == ")":
#         count_balanced += 1
# if count_unbalanced == count_balanced:
#     print("BALANCED")
# else:
#     print()

iterations = int(input())

opening_brackets = 0
closing_brackets = 0

for i in range(iterations):
    symbol = input()
    if symbol == "(":
        opening_brackets += 1
    elif symbol == ")":
        closing_brackets += 1
    if closing_brackets > opening_brackets:
        break
    if opening_brackets - closing_brackets > 1:
        break

if opening_brackets != closing_brackets:
    print("UNBALANCED")
else:
    print("BALANCED")