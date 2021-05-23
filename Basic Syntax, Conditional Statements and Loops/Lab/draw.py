n = int(input())

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print()
for m in range(n - 1, - 1, -1):
    for g in range(0, m):
        print("*", end="")
    print()
