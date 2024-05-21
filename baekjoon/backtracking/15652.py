def backtrack(start, combination):
    if len(combination) == M:
        print(' '.join(map(str, combination)))
        return

    for i in range(start, N + 1):
        backtrack(i, combination + [i])

N, M = map(int, input().split())
backtrack(1, [])
        
    