from collections import deque

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

def bfs():
    while queue:
        for _ in range(len(queue)):
            x, y, type = queue.popleft()
            if type == 'J':
                if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                    return visited[x][y] + 1

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny, 'J'))

        for _ in range(len(queue)):
            x, y, type = queue.popleft()
            if type == 'F':
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] in ['J', '.']:
                        matrix[nx][ny] = 'F'
                        queue.append((nx, ny, 'F'))

    return "IMPOSSIBLE"

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'J':
            queue.append((i, j, 'J'))
            visited[i][j] = 1
        elif matrix[i][j] == 'F':
            queue.append((i, j, 'F'))
print(bfs())

