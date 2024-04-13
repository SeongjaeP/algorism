n = int(input())
num_list = list(map(int,input().split()))

dp = [0] * 100

# 1,1 1,5 
# 3, 5 

dp[0] = num_list[0]
dp[1] = max(num_list[1], num_list[0])
#dp[2] = num_list[0] + num_list[2]
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + num_list[i])

print(max(dp[n-1]))



