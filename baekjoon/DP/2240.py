T, W = map(int, input().split())
num_list = [0] + list(int(input()) for _ in range(T))

dp = [[0] * (W + 1) for _ in range(T + 1)]

for i in range(T + 1):
    # 1 번 나무에서 그대로
    if num_list[i] == 1:
        dp[i][0] = dp[i-1][0] + 1

    # 2번에 있을 경우
    else:
        dp[i][0] = dp[i-1][0]

    # 1번 이상 움직이는 경우
    for j in range(1, W + 1):
        # i초에 2번 나무에서 자두가 떨어지고, 현재 2번 나무에 위치
        if num_list[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        # i초에 1번 나무에서 자두가 떨어지고, 현재 1번에 있는 경우
        elif num_list[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

        # i초에 자두가 떨어지는 나무와 현재 나무의 위치가 다름
        else:
            # 움직여서 못 먹는 경우와 움직이지 않아서 못 먹는 경우 비교
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])



print(max(dp[T]))



# 참고 https://wooono.tistory.com/643