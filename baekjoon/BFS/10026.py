import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
graph = [list(input()) for _ in range(n)]


visited = [[0]*n for _ in range(n)]

# 방향 벡터 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, color):
    visited[x][y] = 1  
    for i in range(4):  
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n: 
            continue
        if graph[nx][ny] == color and visited[nx][ny] == 0:  
            dfs(nx, ny, color)

# 적록색약이 아닌 사람
normal_cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, graph[i][j])
            normal_cnt += 1

# 방문 기록 초기화
visited = [[0]*n for _ in range(n)]

# 적록색약인 사람 (R을 G로 변경)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

color_weak_cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, graph[i][j])
            color_weak_cnt += 1

print(normal_cnt, color_weak_cnt)
