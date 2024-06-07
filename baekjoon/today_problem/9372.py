T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    pairs = [tuple(map(int, input().split())) for _ in range(m)]

    # n개의 노드를 연결하는 최소 간선의 수는 항상 n-1
    print(n - 1)