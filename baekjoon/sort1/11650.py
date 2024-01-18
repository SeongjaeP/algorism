N = int(input())

num_list = [tuple(map(int, input().split())) for _ in range(N)]
num_list.sort(key = lambda x : (x[0], x[1]))


for _ in num_list:
    print(_[0], _[1])