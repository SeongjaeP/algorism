N = int(input())

coins = [1,2,5,7]

dp =[float('inf')] * (N + 1)
dp[0] = 0

for i in range(N + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)



print(dp[N])

# N = 12

# 1 2 3 4 5 6 7 8 9 10 11 12
# 1 1 2 2 1 2 1 2


# 3 - 1 = 2