numbers = input().split(", ")
new_list = []

for num in numbers:
    if num == "0":
        numbers.append(num)  # add number at the end
        numbers.remove(num)  # removes number

numbers = [int(i) for i in numbers]
print(numbers)
