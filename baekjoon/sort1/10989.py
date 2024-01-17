import heapq


N = int(input())
num_list = list(int(input()) for _ in range(N))

heapq.heapify(num_list)
sorted_list = [heapq.heappop(num_list) for _ in range(N)]
print('\n'.join(map(str, sorted_list)))


# 할당을 해줘야하는거 같음
import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] > 0:
        for _ in range(num_list[i]):
            print(i)



import sys

N = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i) + '\n')