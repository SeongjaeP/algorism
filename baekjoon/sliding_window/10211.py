T = int(input())

for _ in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    
    current_sum = num_list[0]
    max_sum = num_list[0]
    
    for i in range(1, N):
        current_sum = max(num_list[i], current_sum + num_list[i])
        max_sum = max(max_sum, current_sum)
    
    print(max_sum)
