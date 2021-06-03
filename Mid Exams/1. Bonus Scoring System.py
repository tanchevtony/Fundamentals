import sys
import math

students = int(input()) # number of students enrolled in the course
lectures = int(input()) # total count of the lectures
the_initial_bonus = int(input()) # the initial bonus

max_result = - sys.maxsize
max_attendances = - sys.maxsize
for i in range(students):
    attendance = int(input())

    total_bonus = attendance / lectures * (5 + the_initial_bonus)
    max_bonus = math.ceil(total_bonus / students + the_initial_bonus)
    if max_bonus > max_result:
        max_result = max_bonus
    if attendance > max_attendances:
        max_attendances = attendance

print()