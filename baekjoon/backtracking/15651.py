def backtrack(start, combination):
    if len(combination) == M:
        print(' '.join(map(str, combination)))
        return

    for i in range(1, N + 1):
        backtrack(i + 1, combination + [i])

N, M = map(int, input().split())
backtrack(1, [])