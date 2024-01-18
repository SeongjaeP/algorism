import sys

N = int(sys.stdin.readline())

num_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
num_list.sort(key = lambda x : (x[1], x[0]))


for _ in num_list:
    print(_[0], _[1])