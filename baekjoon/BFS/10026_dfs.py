<<<<<<< HEAD
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(x, y, color):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == color and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, color)


cnt_normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, matrix[i][j])
            cnt_normal += 1



# 적록 색약인 경우
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

cnt_weak = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, matrix[i][j])
            cnt_weak += 1

print(cnt_normal, cnt_weak)
=======
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(x, y, color):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == color and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, color)


cnt_normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, matrix[i][j])
            cnt_normal += 1



# 적록 색약인 경우
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

cnt_weak = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, matrix[i][j])
            cnt_weak += 1

print(cnt_normal, cnt_weak)
>>>>>>> 90bfbcb748efe876e06138552a44766c9e4ce8b4
