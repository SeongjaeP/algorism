from collections import deque

n, m = map(int ,input().split())

map_list = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(n):
    for j in range(m):
        if map_list[i][j] == 0:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    def bfs(x, y):
        visited[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and map_list[nx][ny] == 0:



def  dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if map_list[x][y] == 0:
        map_list[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)