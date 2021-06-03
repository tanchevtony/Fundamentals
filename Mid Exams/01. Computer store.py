price_without_tax = 0
tax = 0
total_price = 0

flag = True
command = input()
while command != "special" and command != "regular":
    price = float(command)

    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    price_without_tax += price
    tax += price * 0.2
    total_price = price_without_tax + tax

    command = input()
if command == "special":
    total_price *= 0.9
if total_price == 0:
    print("Invalid order!")
    flag = False

if flag:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_tax}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

# 50/100


# 1050
# 200
# 450
# 2
# 18.50
# 16.86
# special

# 1023
# 15
# -20
# -5.50
# 450
# 20
# 17.66
# 19.30
# regular
