my_list = []
for symbol in range(2):
    number = int(input())
    my_list.append(number)
for index in range(my_list[0], my_list[1] + 1):
    print(chr(index), end=' ')

# variant 2

start = int(input())
end = int(input())

for number in range(start, end + 1):
    print(chr(number), end=" ")