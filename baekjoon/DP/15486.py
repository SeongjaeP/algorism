import sys

N = int(sys.stdin.readline().strip())
T_and_P = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [0] * (N + 1)
max_value = 0

for i in range(N):
    max_value = max(max_value, dp[i])
    if i + T_and_P[i][0] <= N:
        dp[i + T_and_P[i][0]] = max(dp[i + T_and_P[i][0]], max_value + T_and_P[i][1])



print(max(dp))
    #  < N 이면 break 걸어주는 조건 마지막에