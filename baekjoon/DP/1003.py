<<<<<<< HEAD
T = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])


# 피보나치에 대해 이해하면 쉽게 접근 가능할 듯
# 2차원으로 dp리스트 만들어서도 ㄱㄴ
# 따로따로 만들어서도 가능
    

=======
zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())
    
for _ in range(T):
    fibonacci(int(input()))
>>>>>>> 9b524a8380b029d5f724bc9c39254e4b0fe3e284
