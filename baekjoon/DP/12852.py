<<<<<<< HEAD
# X // 3 == 0  X / 3
# X // 2 == 0 X / 2
# X - 1 

N = int(input())
dp = [0] * 10^6
pre_dp = [0] * 10^6

def calculate(X):
    if X // 3 == 0:
        X = X / 3

    if X // 2 == 0:
        X = X / 2


=======
N = int(input())

dp = [0] * (N + 1)
path = [0] * (N + 1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    path[i] = i - 1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        path[i] = i // 2
    
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        path[i] = i // 3


print(dp[N])
answer = []
while N > 0:
    answer.append(N)
    N = path[N]
print(' '.join(map(str, answer)))
>>>>>>> b660b3c62341c6e964ceedd2526530bb760fb414
