# 자기보다 작은 것만 먹을 수 있음.
from bisect import bisect_left
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_list.sort()
    B_list.sort()


    result = 0
    for a in A_list:
        result += bisect_left(B_list, a)

    print(result)







# from bisect import bisect_left, bisect_right
#
# nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6]
# n = 5
#
# print(bisect_left(nums, n))
# print(bisect_right(nums, n))
