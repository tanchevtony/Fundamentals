number = int(input())

flag = False
if number > 1:
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            flag = True
            break
if flag:
    print("False")
else:
    print("True")