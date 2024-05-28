<<<<<<< HEAD
from collections import deque

n = int(input())
original_matrix = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited, matrix):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[x][y] == matrix[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_regions(matrix):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited, matrix)
                count += 1
    return count

# 적록색약이 아닌 경우
cnt1 = count_regions(original_matrix)

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if original_matrix[i][j] == 'R':
            original_matrix[i][j] = 'G'

cnt2 = count_regions(original_matrix)

print(cnt1, cnt2)
=======
from collections import deque

n = int(input())
original_matrix = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited, matrix):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[x][y] == matrix[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_regions(matrix):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited, matrix)
                count += 1
    return count

# 적록색약이 아닌 경우
cnt1 = count_regions(original_matrix)

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if original_matrix[i][j] == 'R':
            original_matrix[i][j] = 'G'

cnt2 = count_regions(original_matrix)

print(cnt1, cnt2)
>>>>>>> 90bfbcb748efe876e06138552a44766c9e4ce8b4
