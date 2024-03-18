N, M = map(int, input().split())
light_list = list(map(int, input().split()))
task_list = [list(map(int, input().split())) for _ in range(M)]


for i in range(M):
    op, a, b = task_list[i]
    if op == 1:
        light_list[a-1] = b
    elif op == 2:
        for j in range(a-1, b):
            light_list[j] = 1 - light_list[j]
    elif op == 3:
        for j in range(a-1, b):
            light_list[j] = 0
    elif op == 4:
        for j in range(a-1, b):
            light_list[j] = 1
            

print(' '.join(map(str,light_list)))