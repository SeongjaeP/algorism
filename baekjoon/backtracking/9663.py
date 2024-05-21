N = int(input())

# 열, 대각선 두 개, 즉 총 세 개의 리스트에서 false면 추가하고 다시 false로

used_column = [False] * N
used_pos_dia = [False] * (2*(N-1) + 1)
used_neg_dia = [False] * (2*(N-1) + 1)
#arr_matrix = [[0] * N for _ in range(N)]
cnt = 0

def solution(K):
    global N, cnt

    if K == N:
        cnt += 1
        return
    
    for i in range(N):
        if not used_column[i] and not used_neg_dia[(N-1) + K - i] and not used_pos_dia[K+i]:
            used_column[i] = True
            used_neg_dia[(N-1) + K - i] = True
            used_pos_dia[K+i] = True
            solution(K + 1)
            used_column[i] = False
            used_neg_dia[(N-1) + K - i] = False
            used_pos_dia[K+i] = False


solution(0)
print(cnt)