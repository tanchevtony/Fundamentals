# number = int(input())
# num = str(number)
# new_num = int(''.join(sorted(num, reverse=True)))
# print(new_num)

# version 2

number = list(input())
number.sort(reverse=True)
print("".join(number))
