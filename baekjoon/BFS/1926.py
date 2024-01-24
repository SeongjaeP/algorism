from collections import deque

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    size = 1

    while queue:
        x, y =queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                size += 1
    return size

max_size = 0
count = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))
            count += 1


print(count)
print(max_size)



# DFS
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global size
    size += 1
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

max_size = 0
count = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            size = 0
            dfs(i, j)
            max_size = max(max_size, size)
            count += 1

print(count)
print(max_size)
