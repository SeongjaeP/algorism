from collections import deque

# BFS 알고리즘을 사용하여 최소 이동 횟수를 계산하는 함수
def bfs(start_x, start_y, destination_x, destination_y, n, visited):
    # 나이트가 이동할 수 있는 8가지 방향
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        # 목적지에 도착한 경우 이동 횟수를 반환
        if x == destination_x and y == destination_y:
            return visited[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1  # 목적지에 도달할 수 없는 경우 (이론상 발생하지 않음)

# 테스트 케이스의 수 T를 입력받음
T = int(input())

for _ in range(T):
    # 체스판의 크기 n, 시작 위치 (start_x, start_y), 도착 위치 (destination_x, destination_y) 입력 받음
    n = int(input())
    start_x, start_y = map(int, input().split())
    destination_x, destination_y = map(int, input().split())
    visited = [[0] * n for _ in range(n)]
    visited[start_x][start_y] = 1

    # 시작 위치와 도착 위치가 같은 경우 바로 0 출력
    if start_x == destination_x and start_y == destination_y:
        print(0)
    else:
        print(bfs(start_x, start_y, destination_x, destination_y, n, visited))
