import sys
input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    scores = [list(map(int, data[i*2+1:i*2+3])) for i in range(n)]
    
    # 최대 연속 행을 저장하는 배열
    continuity = [[0] * 6 for _ in range(n)]
    
    # 초기화
    for i in range(6):
        if scores[0][0] == i or scores[0][1] == i:
            continuity[0][i] = 1
    
    # 연속 행 계산
    for i in range(1, n):
        for j in range(6):
            if scores[i][0] == j or scores[i][1] == j:
                if scores[i-1][0] == j or scores[i-1][1] == j:
                    continuity[i][j] = continuity[i-1][j] + 1
                else:
                    continuity[i][j] = 1
    
    # 최대 연속 행과 해당 평가 점수 찾기
    max_count = 0
    grade = 0
    for i in range(n):
        for j in range(6):
            if continuity[i][j] > max_count:
                max_count = continuity[i][j]
                grade = j
    
    print(max_count, grade)

if __name__ == "__main__":
    solve()
