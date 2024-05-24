N, M = map(int, input().split())
num_list = list(int(input()) for _ in range(N))

num_list.sort()
#print(num_list)

result = float('INF')

left = 0
right = 0

while left <= right and right < N:
    difference = num_list[right] - num_list[left]

    if difference >= M:
        result = min(result, difference)
        left += 1
        
    else:
        right += 1
        
print(result)

# m = 3
# 3 5 10