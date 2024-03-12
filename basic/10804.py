arr = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    arr[a:b+1] = reversed(arr[a:b+1])

print(' '.join(map(str, arr[1:])))