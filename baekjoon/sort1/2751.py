import sys

N = int(sys.stdin.readline().strip())
num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

sorted_list = sorted(num_list)

print('\n'.join(map(str, sorted_list)))
