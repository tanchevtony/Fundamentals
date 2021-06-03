lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
for day in range(1, lost_fights_count + 1):

    if day % 2 == 0:
        broken_helmet += 1
    if day % 3 == 0:
        broken_sword += 1
    if broken_helmet and broken_sword > 1:
        broken_shield += 1
    if broken_shield > 2:
