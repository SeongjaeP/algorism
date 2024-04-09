from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
num_list = list(map(int, input().split()))


# binary search 말곤 생각이 안남


# O(logN)으로 설계해야함.

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

count = count_by_range(num_list, m, m)

if count == 0:
    print(-1)
else:
    print(count)