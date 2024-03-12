
import sys

N = int(sys.stdin.readline())
cost = [list(map(int ,sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

# R  G  B  
# 
# 3
# 26 40 83``
# 49 60 57
# 13 89 99

# 1번 집의 색은 2번 집 색과 달라야 함
# N번 집의 색은 N - 1번 집 색과 달라야 함
# i번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 함.


