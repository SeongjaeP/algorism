import sys

N = int(sys.stdin.readline())
input_list = [list(sys.stdin.readline().split()) for _ in range(N)]

input_list.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in input_list:
    print(i[0])