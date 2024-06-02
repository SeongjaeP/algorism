n = int(input())
num_list = list(map(int, input().split()))


# 7
# 15 11 4 8 5 2 4


# 6 
# 13 42 5 7 6 2
# 가장 긴 증가하는 부분 수열(LIS)


num_list.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))