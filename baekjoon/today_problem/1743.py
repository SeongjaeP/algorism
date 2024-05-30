from collections import deque


def bfs(start, visited, graph):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    area_size = 0

    while queue:
        x, y = queue.popleft()
        area_size += 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return area_size


def solution(n, m, k, trash_pos):
    graph = [[0] * m for _ in range(n)]
    for r, c in trash_pos:
        graph[r - 1][c - 1] = 1

    
    visited = [[False] * m for _ in range(n)]
    max_area = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                max_area = max(max_area, bfs((i, j), visited, graph))

    return max_area


n, m, k = map(int, input().split())
trash_pos = [tuple(map(int, input().split())) for _ in range(k)]
print(solution(n, m, k, trash_pos))