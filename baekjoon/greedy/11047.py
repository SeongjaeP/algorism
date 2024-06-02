N, K = map(int, input().split())

coin_list = [int(input()) for _ in range(N)]

cnt = 0
for coin in reversed(coin_list):
    if coin <= K:
        cnt += K // coin
        K %= coin
    
    if K == 0:
        break

print(cnt)