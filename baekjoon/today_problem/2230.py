n, m = map(int, input().split())
num_list = list(int(input()) for _ in range(n))


#result = []
num_list.sort()
result = float('inf')

left = 0
right = 0

while right < n:
    if num_list[right] - num_list[left] >= m:
        result = min(result, num_list[right] - num_list[left])
        left += 1
        if left > right:
            right = left
    else:
        right += 1
        if right >= n:
            break

print(result)
            




            # 1 3 5 
            # 3 5