product_name = input().lower()
quntity = float(input())

def orders_calc(product, quantity):

    result = None
    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity * 1
    elif product == "coke":
        result = quntity * 1.4
    elif product == "snacks":
        result = quntity * 2
    print(f"{result:.2f}")
# result formatted to the second decimal place!
orders_calc(product_name, quntity) 


