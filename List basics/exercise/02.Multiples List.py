factor = int(input())
count = int(input())

new_list = []

for num in range(1, count + 1):
    new_list.append(num * factor)

print(new_list)