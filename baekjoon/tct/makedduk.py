from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
#4, 6이면 
# 19 15 10 17
# 남기는 것을 다 더해서 6으로 만들어야 함.

start = 0
end = max(num_list)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in num_list:
        if x > mid:
            total += x - mid

    if total < M:
         end = mid - 1

    else:
            result = mid
            start = mid + 1

print(result)