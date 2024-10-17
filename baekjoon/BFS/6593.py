from collections import deque
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    
    board = [[list(input().strip()) for _ in range(R)] for _ in range(L)]
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]

    queue = deque()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == 'S':
                    queue.append((0, i, j, k))
                    visited[i][j][k] = True


    def bfs():
        while queue:
            cnt, z, x, y = queue.popleft()

            if board[z][x][y] == 'E':
                return f"Escaped in {cnt} minute(s)."
                break

            for dz, dx, dy in direction:
                nz = z + dz
                nx = x + dx
                ny = y + dy

                if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny] and board[nz][nx][ny] != '#':
                    queue.append((cnt + 1, nz, nx, ny))
                    visited[nz][nx][ny] = True

        return "Trapped!"

    print(bfs())