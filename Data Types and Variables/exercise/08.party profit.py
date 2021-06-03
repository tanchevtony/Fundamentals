# party_size = int(input())
# days = int(input())
#
# coins = 0
#
# for day in range(1, days + 1):
#
#     if day % 10 == 0:
#         party_size -= 2
#
#     if day % 15 == 0:
#         party_size += 5
#
#     coins += 50 - (party_size * 2)
#
#     if day % 3 == 0:
#         coins -= party_size * 3
#
#     if day % 5 == 0:
#         coins += party_size * 20
#         if day % 3:
#             coins -= party_size * 2
#
# profit_companions = coins / party_size
# print(f"{party_size} companions received {profit_companions:.0f} coins each ")


party_size = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coins += 50 - 2 * party_size
    if day % 3 == 0:
        coins -= 3 * party_size
    if day % 5 == 0:
        coins += 20 * party_size
        if day % 3 == 0:
            coins -= 2 * party_size
coins_profit = coins // party_size
print(f"{party_size} companions received {coins_profit} coins each.")