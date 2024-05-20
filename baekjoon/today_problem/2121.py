import sys
n = int(sys.stdin.readline())
A, B = map(int,input().split())

data = set()

for _ in range(n):
    data.add(tuple(map(int, sys.stdin.readline().split())))


cnt = 0
for i in data:
    if (i[0] + A, i[1]) in data and (i[0], i[1] + B) in data and (i[0] + A, i[1] + B) in data:
        cnt += 1

print(cnt)