from collections import deque

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV별 방향 정리
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def check(row, col):
    return row < 0 or row >= N or col < 0 or col >= M

def init():
    global space
    obj = deque()
    answer = 0
    for i in range(N):
        for j in range(M):
            if space[i][j] != 6 and space[i][j] != 0:
                obj.append((space[i][j], i, j))
            if space[i][j] == 0:
                answer += 1
    return obj, answer

# cctv좌표들, 빈칸 개수 초기화
cctv, answer = init()

def move(x, y, direc, space_copy):
    for d in direc:
        nx, ny = x, y

        while True:
            nx += dx[d]
            ny += dy[d]

            if check(nx, ny) or space_copy[nx][ny] == 6:
                break
            if space[nx][ny] == 0:
                space_copy[nx][ny] = '#'


def zero_cnt(space_copy):
    global answer
    cnt = 0
    for i in space_copy:
        cnt += i.count(0)
    answer = min(answer, cnt)

def dfs(level, space):
    space_copy = [[j for j in space[i]] for i in range(N)]

    if level == len(cctv):
        zero_cnt(space_copy)
        return
    number, x, y = cctv[level]

    for d in direction[number]:
        move(x, y, d, space_copy)
        dfs(level+1, space_copy)
        space_copy = [[j for j in space[i]] for i in range(N)]

dfs(0, space)
print(answer)