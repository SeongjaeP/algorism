from collections import deque

n, m = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if map_list[nx][ny] == 1:
                map_list[nx][ny] = map_list[x][y] + 1
                queue.append((nx, ny))

    return map_list[n - 1][m - 1]





# 결과랑 전꺼랑 계속 비교해서 min처리 해서 최솟값 뽑아내기 그냥 가는곳에 + 1 더하면 됨