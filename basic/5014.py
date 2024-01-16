from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)
queue = deque([(S, 0)])  
visited[S] = True

while queue:
    current, cnt = queue.popleft()
    if current == G:
        print(cnt)
        break

    if current + U <= F and not visited[current + U]:
        visited[current + U] = True
        queue.append((current + U, cnt + 1))

    if current - D > 0 and not visited[current - D]:
        visited[current - D] = True
        queue.append((current - D, cnt + 1))
else:
    print("use the stairs")
