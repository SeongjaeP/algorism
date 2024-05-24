N, M = map(int, input().split())

num_list = list(map(int, input().split()))

left = 0
right = 0
current_sum = 0
cnt = 0

while right <= N:
    if current_sum == M:
        cnt += 1
        current_sum -= num_list[left]
        left += 1
    
    elif current_sum < M:
        if right < N:
            current_sum += num_list[right]
        right += 1
          

    else:
        current_sum -= num_list[left]
        left += 1
        


print(cnt)
