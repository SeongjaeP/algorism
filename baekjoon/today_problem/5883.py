n = int(input())

num_list = [int(input()) for _ in range(n)]
a = set(num_list)
result = []
for i in a:
    b = [x for x in num_list if x != i]
    
    max_len = 0
    current_len = 1

    for k in range(1, len(b)):
        if b[k] == b[k - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1

    if current_len > max_len:
        max_len = current_len

    result.append(max_len)

print(max(result))