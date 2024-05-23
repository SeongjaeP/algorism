N, S = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

# 1 2 3 4 5 5 7 8 9 10

left = 0
right = 0
current_sum  = num_list[0]
length_min = float('INF')

while right < N:
    # 이 부분 시간초과 발생
    #list_sum = sum(num_list[left:right+1])
    if current_sum >= S:
        length_min = min(length_min, right - left + 1)
        current_sum -= num_list[left]
        left += 1
    else:
        right += 1
        if right < N:
            current_sum += num_list[right]

if length_min == float('INF'):
    print(0)
else:
    print(length_min)

# 1 2 3 4 5 5 7 8 9 10
# 15
# 1 1 1
# 1 2 3
# 1 2 3          6
# 1 2 3 4        10
# 1 2 3 4 5      15                 5
# 2 3 4 5        14                 
# else 2 3 4 5 5      19
# 3 4 5 5      17              4      
# 4 5 5        14  
# 4 5 5 7      21
# 5 5 7                      4
#    5 7                     3
# 5 7 8         20 
# 7 8          15            2
# 7 8 9       ~           2
# 89              
# 9 10 
