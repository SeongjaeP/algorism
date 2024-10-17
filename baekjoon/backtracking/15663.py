N, M = map(int,input().split())

num_list = sorted(list(map(int, input().split())))
visited = [False] * N
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    

    prev_num = None
    for i in range(N):
        if not visited[i] and num_list[i] != prev_num:
            visited[i] = True
            result.append(num_list[i])
            dfs()
            result.pop()
            visited[i] = False
            prev_num = num_list[i]

dfs()