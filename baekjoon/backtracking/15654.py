N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

def backtrack(start, combination):
    if len(combination) == M:
        print(' '.join(map(str, combination)))
        return
    
    for i in range(1, N + 1):
        for j in num_list:
            backtrack(j, combination + )


backtrack(num_list[0], [])


# 4 5 2 -> 2 4 5
# (2, [])
