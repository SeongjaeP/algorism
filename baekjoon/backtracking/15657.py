N, M = map(int,input().split())
num_list = sorted(map(int,input().split()))

result = []

def dfs(start):
    if len(result) == M:
        print(*result)
        return 
    
    for i in range(start,N):
        result.append(num_list[i])
        dfs(i)
        result.pop()
        


dfs(0)

