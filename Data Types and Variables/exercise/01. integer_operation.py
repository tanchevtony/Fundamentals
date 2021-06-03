new_list = []
for number in range(0,4):
    num = int(input())
    new_list.append(num)
total_sum = (int((new_list[0] + new_list[1]) / new_list[2]) * new_list[3])
print(total_sum)
