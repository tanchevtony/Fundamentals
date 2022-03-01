input_operator = input().lower()  # # .lower (regardless of the input), multiply, divide, add, subtract
first_num = int(input())
second_num = int(input())


def calc(operator, num_1, num_2):
    if operator == 'multiply':
        return num_1 * num_2
    elif operator == 'divide':
        return num_1 // num_2  # // to return integer, / will return float
    elif operator == 'add':
        return num_1 + num_2
    elif operator == 'subtract':
        return num_1 - num_2


print(calc(input_operator, first_num, second_num))


# second solution

input_operator = input().lower()  # .lower (regardless of the input), multiply, divide, add, subtract
first_num = int(input())
second_num = int(input())


def calc(operator, num_1, num_2):
    result = None
    if operator == 'multiply':
        result = num_1 * num_2
    elif operator == 'divide':
        result = int(num_1 / num_2)  # to return integer
    elif operator == 'add':
        result = num_1 + num_2
    elif operator == 'subtract':
        result = num_1 - num_2
    return result


print(calc(input_operator, first_num, second_num))
