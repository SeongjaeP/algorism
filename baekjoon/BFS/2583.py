from collections import deque

M, N, K = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(K)]

visited = [[0] * N for _ in range(M)]

for matrix in num_list:
    x1, y1, x2, y2 = matrix[0], matrix[1], matrix[2], matrix[3]
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = -1  
    size = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = -1
                queue.append((nx, ny))
                size += 1

    result.append(size)

result = []

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
