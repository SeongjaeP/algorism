# 불이 방문한거랑 상근이가 방문한거랑 각각을 리스트로 만들어서 할수도 있을거 같고
# 아니면 방문처리를 1, 2 이렇게 다르게 해서 예를 들어 불이 지나간 자리르 2면 
# 위와 같이 방문처리를 하면 메모리는 줄일 수 있지만, 코드가 난잡해져서 비추라고 함
# 그래도 하나의 visited으로 해보겠음
from collections import deque

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    cnt = 0
    while sq:
        cnt += 1
        # 불 먼저 확산
        for _ in range(len(fq)):
            fx, fy = fq.popleft()
            for i in range(4):
                nfx, nfy = fx + dx[i], fy + dy[i]
                if 0 <= nfx < N and 0 <= nfy < M and matrix_map[nfx][nfy] == '.' and visited[nfx][nfy] == 0:
                    visited[nfx][nfy] = 2
                    fq.append((nfx, nfy))

        # 상근이 이동
        for _ in range(len(sq)):
            sx, sy = sq.popleft()
            for i in range(4):
                nsx, nsy = sx + dx[i], sy + dy[i]
                if 0 <= nsx < N and 0 <= nsy < M:
                    if matrix_map[nsx][nsy] == '.' and visited[nsx][nsy] == 0:
                        visited[nsx][nsy] = 1
                        sq.append((nsx, nsy))
                else:
                    return cnt
    return 'IMPOSSIBLE'

for _ in range(T):
    M, N = map(int, input().split())
    matrix_map = [list(input().strip()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    fq = deque()
    sq = deque()

    for i in range(N):
        for j in range(M):
            if matrix_map[i][j] == '*':
                fq.append((i, j))
                visited[i][j] = 2
            elif matrix_map[i][j] == '@':
                sq.append((i, j))
                visited[i][j] = 1

    result = bfs()
    print(result)
