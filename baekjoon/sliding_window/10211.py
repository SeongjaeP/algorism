T = int(input())


for _ in range(T):
    N = int(input())
    num_list = [0] * N +list(map(int, input().split())) + [0] * N
    end = 3 * N
    step = N
    window = sum(num_list[:step-1])
    answer = window
    for i in range(step, end):
        window += num_list[i] - num_list[i-step]
        answer = max(answer, window)
    
    print(answer)
