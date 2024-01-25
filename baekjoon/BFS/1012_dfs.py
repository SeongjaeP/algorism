# dfs로 풀기. 재귀
import sys
sys.setrecursionlimit(10000)
T = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if matrix[x][y] == 1:
            matrix[x][y] = 0

            for i in range(4):
                dfs(x + dx[i], y + dy[i])

            return True
        return False
    return False

for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j): # dfs에서 True를 반환하면, 새로운 배추 그룹을 찾은 것
                cnt += 1 # 배추 그룹의 개수를 1 증가
    print(cnt) # 필요한 지렁이의 최소 개수 출력