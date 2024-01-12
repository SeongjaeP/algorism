num_list = list(int(input()) for _ in range(7))
result = [i for i in num_list if i % 2 == 1]


if not result:
    print(-1)
else:
    print(sum(result))
    print(min(result))
