N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def can_slope(line, L):
    length = len(line)
    used = [False] * length

    for i in range(length - 1):
        if line[i] == line[i + 1]:
            continue
        
        elif abs(line[i] - line[i+1]) == 1:
            # 올라가는 경사로
            if line[i] < line[i+1]:
                for j in range(L):
                    if i - j < 0 or line[i] != line[i - j] or used[i - j]:
                        return False
                    used[i - j] = True
            # 내려가는 경사로 
            else:
                for j in range(L):
                    if i + 1 + j >= length or line[i + 1] != line[i + 1 + j] or used[i + 1 + j]:
                        return False
                    used[i + 1 + j] = True

        else:
            return False
        
    return True

def count_possible_slopes(grid, L):
    count = 0
    
    for row in grid:
        if can_slope(row, L):
            count += 1
    
    for col in zip(*grid):
        if can_slope(col, L):
            count += 1
    
    return count

print(count_possible_slopes(grid, L))

