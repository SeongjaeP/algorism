# 처음 아기 상어의 크기는 2, 1초에 상하좌우로 이동
# 자기보다 높으면 지나갈 수 없음. 자기보다 작은 물고기만 먹을 수 있고
# 자기랑 똑같은 물고기는 먹을 수 없지만, 움직이기는 가능

# 먹을 수가 없다? -> 엄마 상어에게 도움
# 먹을 수 있는 물고기가 1마리 ? 물고기 먹으러감
# 1마리 보다 많으면 가장 가까운 물고기 먹으러 감
# 거리는 최솟값으로 가야함
# 가까운 물고기가 많다면, 가장 위에 있는 물고기
# 여러마리면, 가장 왼쪽에 있는 물고기 먹기

# 먹으면 빈칸이 됨
# 자신의 크기와 같은 수의 물고기를 먹을 떄 마다 크기가 1증가. 
# 예를 들어, 크기가 2인 아기 상어가 물고리를 두 마리 먹으면 크기가 3됨

from collections import deque

N = int(input())
matrix_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

queue = deque((x,y))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(N):
    for j in range(N):
        if matrix_map[i][j] == 9:
            queue.append((i, j))

# 1이 여러개면
cnt = 0

def bfs(x, y):
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if matrix_map[x][y] > matrix_map[nx][ny] and matrix_map[nx][ny] != 0:
                    visited[nx][ny] = visited[]
            


