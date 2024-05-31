
H, Y = map(int, input().split())


money = [0] * (Y + 1)
money[0] = H

for i in range(1, Y + 1):
    money[i] = max(money[i], int(money[i - 1] * 1.05))

    if i >= 3:
        money[i] = max(money[i], int(money[i - 3] * 1.2))

    if i >= 5:
        money[i] = max(money[i], int(money[i - 5] * 1.35))

print(money[Y])
