import sys
input = sys.stdin.read

def floyd_warshall(n, graph):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                # 1 1             1 1        11
                # 1 2              1 1       1 2

data = input().split()
n = int(data[0])
index = 1
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

while True:
    a, b = int(data[index]), int(data[index + 1])
    index += 2
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

floyd_warshall(n, graph)

scores = [max(graph[i][1:]) if i != 0 else float('inf') for i in range(n + 1)]
min_score = min(scores)
    
    # 점수가 최소인 회원 찾기
candidates = [i for i in range(1, n + 1) if scores[i] == min_score]
    
print(min_score, len(candidates))
print(' '.join(map(str, candidates)))