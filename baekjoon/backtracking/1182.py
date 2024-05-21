from itertools import combinations

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

num_sum = 0
cnt = 0

for i in range(1, N + 1):
    a = combinations(num_list, i)
    for j in a:
        if sum(j) == S:
            cnt += 1


print(cnt)



##################################################
# 백트래킹 풀이
def backtrack(idx, current_sum):
    global cnt

    if idx == N:
        if current_sum == S:
            cnt += 1
        return
    

    backtrack(idx + 1, current_sum + num_list[idx])
    backtrack(idx + 1, current_sum)

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0

backtrack(0, 0)

print(cnt if S != 0 else cnt - 1)