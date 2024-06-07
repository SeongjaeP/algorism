from collections import deque

n, m = map(int, input().split())

ice_map = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melt_icebergs(ice_map, n, m):
    melt_amount = [[0] * m for _ in range(n)]
    ice_positions = []  # 빙산 위치 저장

    for x in range(n):
        for y in range(m):
            if ice_map[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and ice_map[nx][ny] == 0:
                        cnt += 1
                melt_amount[x][y] = cnt
                if cnt > 0:
                    ice_positions.append((x, y))

    for x, y in ice_positions:
        ice_map[x][y] -= melt_amount[x][y]
        if ice_map[x][y] < 0:
            ice_map[x][y] = 0

    return ice_positions

def bfs(start_x, start_y, visited, ice_map, n, m):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and ice_map[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_icebergs(ice_map, n, m):
    visited = [[False] * m for _ in range(n)]
    iceberg_count = 0

    for i in range(n):
        for j in range(m):
            if ice_map[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited, ice_map, n, m)
                iceberg_count += 1

    return iceberg_count

years = 0

while True:
    ice_positions = melt_icebergs(ice_map, n, m)
    years += 1
    total_iceberg_count = count_icebergs(ice_map, n, m)

    if total_iceberg_count == 0:
        print(0)
        break
    elif total_iceberg_count >= 2:
        print(years)
        break
