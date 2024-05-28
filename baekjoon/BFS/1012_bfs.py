from collections import deque
import sys
T = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0
    return

for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)


















# M, N, K = map(int,input().split())
# for _ in range(T):
#
#     baechu_matrix = [tuple(map(int, input().split())) for _ in range(K)]
#     matrix = [[0] * M for _ in range(N)]
#     visited = [[False] * M for _ in range(N)]
#
#     # 배추 위치 표시
#     for x, y in baechu_matrix:
#         matrix[y][x] = 1
#
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#     def bfs(y, x):
#         queue = deque()
#         queue.append((y, x))
#         visited[y][x] = True
#         size = 1
#
#         while queue:
#             x, y = queue.popleft()
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1 and not visited[ny][nx]:
#                     visited[ny][nx] = True
#                     queue.append((ny, nx))
#                     size += 1
#
#         return size
#
#     min_size = 0
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] == 1 and not visited[i][j]:
#                 min_size = min(min_size, bfs(i,j))
#                 cnt += 1
#
#
#     print(cnt)
#     print(min_size)