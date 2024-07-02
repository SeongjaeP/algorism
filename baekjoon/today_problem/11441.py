n = int(input())
num_list = list(map(int,input().split()))
M = int(input())


for _ in range(M):
    i, j = map(int,input().split())
    print(sum(num_list[i-1:j]))


import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))

num_sum = [0] * (n + 1)
for i in range(1, n+1):
    num_sum[i] = num_sum[i-1] + num_list[i-1]

M = int(input())
for _ in range(M):
    i, j = map(int,input().split())

    print(num_sum[j] - num_sum[i-1])