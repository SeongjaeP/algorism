# 에라토스테네스의 체 알고리즘 

def generator_prime_num(x):
    is_prime = [True] * (x + 1)
    primes = []
    for i in range(2, x + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, x + 1, i):
                is_prime[j] = False
    return primes

N = int(input())

if N == 1:
    print(0)
else:
    result = generator_prime_num(N)

    left = 0
    right = 0
    current_sum = 0
    cnt = 0

    while right <= len(result):
        if current_sum == N:
            cnt += 1
            current_sum -= result[left]
            left += 1
        elif current_sum > N:
            current_sum -= result[left]
            left += 1
        else:
            if right < len(result):
                current_sum += result[right]
            right += 1

    print(cnt)
