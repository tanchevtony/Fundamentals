code = input().split()
string = input()
string = [x for x in string]  # прави лист от вторият вход(изречение) и го разделя буква по буква
message = []
for symbol in code:  # прави лист и разделя първият вход на 3 части
    char = [int(x) for x in symbol]  # объща стринговете в числа
    if len(string) < sum(char)+1:  # ако дължината на string е по малка от сумата на char + 1 (защото индекса започва от нула)
        index = sum(char) - len(string)
    else:
        index = sum(char)
    message.append(string[index])  # add to the list
    string.pop(index)  # remove but keep the value
print("".join(message))