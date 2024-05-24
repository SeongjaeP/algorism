N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

def backtrack(combination):
    if len(combination) == M:
        print(' '.join(map(str, combination)))
        return
    
    for i in range(N):
        for j in num_list:
            backtrack(combination, [num_list[i]])


backtrack(num_list[0], [])


# 4 5 2 -> 2 4 5
# (2, [])
