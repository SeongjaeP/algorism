N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

max_height = max(max(row) for row in matrix)

for rain_height in range(max_height + 1):
