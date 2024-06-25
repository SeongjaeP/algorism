M, N = map(int,input().split())

snack_list = list(map(int, input().split()))

start = 1
end = max(snack_list)

answer = 0
while start <= end:
    mid = (start + end) // 2
    c = 0
    c = sum(snack_list) // mid
    if c >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)


# M > N 이러면 


# 5 3
# 10 10 15
