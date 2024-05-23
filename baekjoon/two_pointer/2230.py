N, M = map(int, input().split())
num_list = list(int(input()) for _ in range(N))

num_list.sort()
#print(num_list)

result = float('INF')

left = 0
right = 0
# 재귀 돌려야함.
while right < N:
    difference = num_list[right] - num_list[left]
    if difference >= M:
        result = min(result, difference)
        left += 1
            # 두 수가 같으면 end를 옆으로 
    else:
        right += 1
        
print(result)