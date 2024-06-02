N = int(input())

plans = input().split()

x, y = (1, 1)

for i in plans:
    if i == 'R' and x != 5:
        x += 1
    elif i == 'U' and y != 1:
        y += 1
    elif i == 'L' and x != 1:
        x -= 1
    elif i == 'D' and y != 5:
        y += 1

print(x, y)


# method 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dr = ['U', 'R', 'D', 'L']

for plan in plans:
    for i in len(dr):
        if plan == dr[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)
