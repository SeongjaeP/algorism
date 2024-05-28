M, N = map(int, input().split())
grid_matrix = [list(map(int, input())) for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    grid_matrix[x][y] = 2
    if x == M - 1:
        return 'YES'
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and grid_matrix[nx][ny] == 0:
            dfs(nx,ny)

    return 'NO'




for j in range(N):
    if grid_matrix[0][j] == 0:
        print(dfs(0, j))
###########################################################################

import sys
sys.setrecursionlimit(1000000)

M, N = map(int, input().split())
grid_matrix = [list(map(int, input())) for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N or grid_matrix[x][y] != 0:
        return False
    if x == M - 1:
        return True
    grid_matrix[x][y] = 2  
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if dfs(nx, ny):
            return True
    return False

result = 'NO'
for j in range(N):
    if grid_matrix[0][j] == 0:
        if dfs(0, j):
            result = 'YES'
            break

print(result)