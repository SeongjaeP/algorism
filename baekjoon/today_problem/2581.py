# 소수 판별 제곱수로 하면 간단함

M = int(input())
N = int(input())

result = []
for i in range(M, N + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        result.append(i)

if not result:
    print(-1)

else:
    print(sum(result))
    print(min(result))



