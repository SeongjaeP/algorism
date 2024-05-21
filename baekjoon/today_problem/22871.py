n = int(input())
num_list = list(map(int,input().split()))


dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
    for j in range(0, i):
        cost = (i - j) * (1 + abs(num_list[i] - num_list[j]))
        dp[j] = min(cost + dp[i], dp[j])



print(min(dp[n-1]))





# 0부터 가는 것 보다 i을 1로 설정해서 
# j는 i보다 작게끔 즉 (0, i)로 설정하면 됨.