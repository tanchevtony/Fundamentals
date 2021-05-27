command = input()
coffee_counter = 0
my_list = ["coding", "CODING", "dog", "DOG", "cat", "CAT", "movie", "MOVIE"]
too_much_coffee = False
while not command == "END":
    if command in my_list:
        if command.isupper():
            coffee_counter += 2
        else:
            coffee_counter += 1
    if coffee_counter > 5:
        too_much_coffee = True
        break
    command = input()
if too_much_coffee:
    print("You need extra sleep")
else:
    print(f"{coffee_counter}")

