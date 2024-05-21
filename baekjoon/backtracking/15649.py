def backtrack(combination):
    if len(combination) == M:
        print(' '.join(map(str, combination)))
        return

    for num in num_list:
        if num not in combination:
            backtrack(combination + [num])

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

backtrack([])