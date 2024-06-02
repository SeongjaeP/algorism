# 어떤 나라에는 N개의 도시가 있음. 각 도시는 보내고자 하는 메시지가 있는 경우, 
# 다론 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 이씅ㅁ
# 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면
# X에서 Y로 향하는 통로가 설치되어 있어야한다. 예를 들어 X에서 Y로 향하는 통로는 있지만,
# Y에서 x로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없음.  


# 

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(start)

count = 0

max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)