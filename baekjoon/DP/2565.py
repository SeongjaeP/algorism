n = int(input())
dp = [1] * n

num_list = [list(map(int, input().split())) for _ in range(n)]
num_list.sort()

for i in range(1, n):
    for j in range(0, i):
        if num_list[j][1] < num_list[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))