number = int(input())
tank_capacity = 250
tank_full = 0

for water in range(number):
    fill_water = int(input())

    if (tank_full + fill_water) > tank_capacity:
        print("Insufficient capacity")
        continue
    else:
        tank_full += fill_water
print(tank_full)