N = int(input())
num_list = [int(input()) for _ in range(N)]

num_list.sort()

max_weight = 0

for i in range(N):
    current_weight = num_list[i] * (N - i)
    if current_weight > max_weight:
        max_weight = current_weight

print(max_weight)