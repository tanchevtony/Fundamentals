import sys
n = int(input())
highest_snowball = - sys.maxsize

for snowball in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow // snowball_time) ** snowball_quality

    if snowball_value > highest_snowball:
        highest_snowball = snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_snow} : {max_snowball_time} = {highest_snowball} ({max_snowball_quality})")

