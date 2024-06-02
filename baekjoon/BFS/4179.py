from collections import deque

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
fire_queue = deque()

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'J':
            queue.append((i, j))
            visited[i][j] = 1
        elif matrix[i][j] == 'F':
            fire_queue.append((i, j))
            matrix[i][j] = 0


def bfs():
    while queue:
        # 먼저 불을 확산시킵니다.
        for _ in range(len(fire_queue)):
            x, y = fire_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == '.':
                    matrix[nx][ny] = 'F'
                    fire_queue.append((nx, ny))

        # 주인공이 이동합니다.
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                return visited[x][y]  # 탈출함
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return "IMPOSSIBLE"


print(bfs())
