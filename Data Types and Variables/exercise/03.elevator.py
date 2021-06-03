import math

capacity = int(input())

number_of_people = int(input())
rest = math.ceil(capacity / number_of_people)

print(rest)
