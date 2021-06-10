my_input = input().split("|")
budget = int(input())
clothes_max_price = 50
shoes_max_price = 35

for word in my_input:
    new_list = word.split("->")
    type_product = new_list[0]
    price_product = int(new_list[1])

    if type_product == "Clothes":
        if price_product <= clothes_max_price:
            budget -= price_product
    elif type_product == "shoes":
        if price_product <= 35:
            budget -= price_product
