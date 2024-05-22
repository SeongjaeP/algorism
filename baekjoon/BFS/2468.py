from collections import deque

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]
flattened_list = [num for sublist in num_list for num in sublist]
# visited = [[0] * N for _ in range(N)]

# 차례대로 털어야해서 최댓값을 가져오는게 좋음. 그래도 다 뒤져봐야할거 아녀 
max_height = max(flattened_list)

# 방문처리랑 num_list를 비교해야겠네 
# max값으로 range해서 잠기면 visited를 -1로 만들고 값을 append
# 그리고 max값으로 뽑아내면 될 듯? 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, height):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and num_list[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
result = 0
# 기존의 result와 비교해서 크면 바꾸고 아니면 계속 
for height in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and num_list[i][j] > height:
                bfs(i, j, height)
                safe_areas += 1

    result = max(result, safe_areas)

print(result)