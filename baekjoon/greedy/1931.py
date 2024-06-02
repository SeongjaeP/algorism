n = int(input())
meeting_list = [tuple(map(int, input().split())) for _ in range(n)]


# 일단 시작점을 기준으로 해야할 것 같음. 아님
# 끝점을 기준으로 해야함
meeting_list.sort(key = lambda x: (x[1], x[0]))

cnt = 0
end_time = 0
for start, end in meeting_list:
    if start >= end_time:
        end_time = end
        cnt += 1
print(cnt)