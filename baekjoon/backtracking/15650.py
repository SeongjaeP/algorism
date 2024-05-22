from itertools import combinations

N, M = map(int, input().split())

a = [i for i in range(1, N + 1)]
b = combinations(a, M)

for j in b:
    print(' '.join(map(str, j)))

###########################################################
# 백트래킹
def backtrack(start, combination):
    if len(combination) == M:
        print(' '.join(map(str, combination)))
        return

    for i in range(start, N + 1):
        backtrack(i + 1, combination + [i])

N, M = map(int, input().split())
backtrack(1, [])