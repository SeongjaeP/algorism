<<<<<<< HEAD
from collections import deque

n = int(input())
matrix = [list(input()) for _ in range(n)]
#visited = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

def bfs(x,y):
    visited[x][y] = 1
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and  matrix[x][y] == matrix[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))


# 적록색약이 아닌 경우
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

# 적록색약인 경우

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)




=======
from collections import deque

n = int(input())
matrix = [list(input()) for _ in range(n)]
#visited = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

def bfs(x,y):
    visited[x][y] = 1
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and  matrix[x][y] == matrix[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))


# 적록색약이 아닌 경우
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

# 적록색약인 경우

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)




>>>>>>> 90bfbcb748efe876e06138552a44766c9e4ce8b4
