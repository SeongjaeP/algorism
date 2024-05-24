from collections import deque

def count_two_friends(n, adj_matrix):
    max_friends = 0

    for i in range(n):
        visited = [False] * n
        visited[i] = True
        queue = deque([(i, 0)])
        friend_count = 0

        while queue:
            current, depth = queue.popleft()
            if depth == 2:
                continue

            for j in range(n):
                if adj_matrix[current][j] == 'Y' and not visited[j]:
                    visited[j] = True
                    queue.append((j, depth + 1))
                    if depth == 0:
                        friend_count += 1

        max_friends = max(max_friends, friend_count)

    return max_friends

n = int(input())
adj_matrix = [input().strip() for _ in range(n)]
print(count_two_friends(n, adj_matrix))


#####################################################################
# 플로이드 워셜
n = int(input())
frineds = [list(input()) for _ in range(n)]

connected = [[0] * n for _ in range(n)]

for k in range(n):
    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            if frineds[i][j] == "Y" or (frineds[i][k] == "Y" and frineds[k][j] == "Y"):
                connected[i][j] = 1

answer = 0
for row in connected:
    answer = max(answer, sum(row))
print(answer)