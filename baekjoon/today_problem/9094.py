T = int(input())

for _ in range(T):
    ans = 0
    n, m = map(int, input().split())
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a**2 + b**2 + m) % (a*b) == 0:
                ans += 1
    print(ans)