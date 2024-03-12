N = int(input())
series_list = list(map(int, input().split()))

dp = [1] * N
# append로 해야하나?

for i in range(N):
    for j in range(i):
        if series_list[i] > series_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))