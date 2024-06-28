N = int(input())



# 뒤에꺼로 sort하고 
meeting_list = [list(map(int, input().split())) for _ in range(N)]

meeting_list.sort(key = lambda x: (x[0], x[1]))

stack = []
result = 0
for i in range(N-1):
    if meeting_list[i][0] + meeting_list[i][1] > meeting_list[i+1][0]:
        result += 1
        stack.append(meeting_list[i])

    


