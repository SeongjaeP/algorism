T = int(input())


def dfs(x):
    visited[x] = True
    num = num_list[x]
    if not visited[num]:
        dfs(num)

for _ in range(T):
    N = int(input())

    num_list = [0] + list(map(int,input().split()))
    visited = [False] * (N+1)
    result = 0
    
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            result += 1
            
    print(result)
    
    

                        
        
        

