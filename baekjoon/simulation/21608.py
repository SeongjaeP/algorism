# 크기 N x N 학생수는 N^2
# (r,c) r행 c 열 맨왼쪽위는 (1, 1)

# 상하좌우에서 갈 수 있으면 인접이라 함

# 1. 
# list 뒤져서 좋아하는 수인지 찾고 
# 상하좌우가 비어있으면 그 자리에서 상하좌우 털어서 빈칸이 가장 많은거
# 행의 번호가 가장 작은 칸 -> 열의 번호가 가장 작은 칸 


# 




N = int(input())

board_map = [[0] * N for _ in range(N)]
student_pref = [list(map(int, input().split())) for _ in range(N**2)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


for student in student_pref:
    result = []
    student_number, prefer_list = student[0], student[1:]

    prefer, empty = 0, 0
    
    for i in range(N):
        for j in range(N):
            # 빈 칸 찾기
            if board_map[i][j] == 0:
                
                # 인접 0이 가장 많은 거와 좋아하는 수 있는 거 찾기
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if student_number in prefer_list:
                            prefer += 1
                        if board_map[nx][ny] == 0:
                            empty += 1
                result.append(i, j, prefer, empty)
    result.sort(key = lambda x:(-x[2], -x[3], x[0], x[1]))
    board_map[result[0][0]][result[0][1]] = student_number


satisfied = [0, 1, 10, 100, 1000]

for i in range(N):
    for j in range(N):
        