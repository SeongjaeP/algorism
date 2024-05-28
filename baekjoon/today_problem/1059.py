L = int(input())
S_range = list(map(int, input().split()))  
n = int(input())

S_range.sort()

if n in S_range:
    print(0)
else:
    lower = 0
    upper = 0
    for S in S_range:
        if S < n:
            lower = S
        elif S > n and upper == 0:
            upper = S
            break  
    result = (n - lower) * (upper - n) - 1
    print(result)
