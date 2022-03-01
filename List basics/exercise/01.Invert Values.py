numbers = input().split(" ")
my_list = [int(i) for i in numbers]
new_negative_list = [-x for x in my_list]
print(new_negative_list)

