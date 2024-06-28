n = int(input())
board_map = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if board_map[j][i] and board_map[i][k]:
                board_map[j][k] = 1

for board in board_map:
    print(*board)