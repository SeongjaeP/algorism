import itertools

N, M = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()

result = itertools.combinations(num_list, M)

for combination in result:
    print(' '.join(map(str, combination)))




# 1 7 8 9


# 1 7 1 8 1 9
# 1
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def dfs(start, cnt):
    if cnt == M:
        print(' '.join(map(str, res)))
        return

    for i in range(start, N):
        res.append(arr[i])
        dfs(i + 1, cnt + 1)
        res.pop()

dfs(0, 0)