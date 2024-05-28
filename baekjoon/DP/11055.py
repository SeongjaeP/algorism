# 증가하는 부분 수열 

N = int(input())
series_list = list(map(int, input().split()))

dp = series_list.copy()

# 1 100 2 1 60
# 증가 끊기면 하나 다시 만들어야함.
for i in range(N):
    for j in range(i):
        if series_list[j] < series_list[i]:
            dp[i] = max(dp[i], dp[j] + series_list[i])

print(max(dp))