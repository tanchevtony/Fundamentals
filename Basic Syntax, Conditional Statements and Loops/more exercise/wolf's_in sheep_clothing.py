# animals = input()
# new_list = animals.split(",")
# new_list = new_list[::-1] #  reverse list
# count_wolfs = 0
# for i, animal in enumerate(new_list):
#     if animal == 'wolf':
#         count_wolfs = i
# if count_wolfs == 0:
#     print("Please go away and stop eating my sheep")
# else:
#     print(f"Oi! Sheep number {count_wolfs}! You are about to be eaten by a wolf!")

animals = input()
new_list = animals.split(", ")
new_list.reverse()
count_wolfs = 0
for i, animal in enumerate(new_list):
    if animal == 'wolf':
        count_wolfs = i
if count_wolfs == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {count_wolfs}! You are about to be eaten by a wolf!")

print(new_list)

