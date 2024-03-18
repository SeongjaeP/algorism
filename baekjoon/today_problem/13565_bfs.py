from collections import deque

M, N = map(int, input().split())
grid_matrix = [list(map(int, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

def bfs():
    queue = deque()
    for i in range(N):
        if grid_matrix[0][i] == 0:
            queue.append((0, i))
            visited[0][i] = 1  


    while queue:
        x, y = queue.popleft()
        if x == M-1:
            return 'YES'

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid_matrix[nx][ny] == 0:
                visited[nx][ny] = 1  
                queue.append((nx, ny))
    return 'NO'

print(bfs())
