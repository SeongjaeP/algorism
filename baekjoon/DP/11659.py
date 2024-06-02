N, M = map(int,input().split())
num_list = list(map(int, input().split()))

dp = [0]
for i in range(1, N + 1):
    dp.append(dp[i-1] + num_list[i-1])

cal_list = [tuple(map(int, input().split())) for _ in range(M)]

for start, end in cal_list:
    print(dp[end] - dp[start-1])