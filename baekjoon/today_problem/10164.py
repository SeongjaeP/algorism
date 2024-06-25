# 32점

from math import factorial
N, M, K = map(int, input().split())

if K == 0:
    print(int(factorial(N+M-2) / (factorial(N-1) * factorial(M-1))))
else:
    x, y = (K//M + 1, K % M)

    a = factorial(x+y-2) / (factorial(x-1) * factorial(y-1))
    b = factorial(N+M-x-y) / (factorial(N-x) * factorial(M-y))
    print(int(a*b))



def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

if K == 0:
    print(comb(N + M - 2, N - 1))
else:
    x, y = (K - 1) // M + 1, (K - 1) % M + 1
    a = comb(x + y - 2, x - 1)
    b = comb((N - x) + (M - y), N - x)
    print(a*b)