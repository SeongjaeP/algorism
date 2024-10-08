def is_inrange(x, y):
    return 1 <= x <= n and 1 <= y <= n

n,m,p,c,d = map(int,input().split())
rudolf = tuple(map(int, input().split()))

points = [0] * (p+1)
pos = [(0,0)] * (p+1)
board_map = [[0] * (n+1) for _ in range(p+1)]
is_live =[False] * (p+1)
stun = [0] * (p+1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board_map[rudolf[0]][rudolf[1]] = -1

for _ in range(p):
    id, x, y = tuple(map(int, input().split()))
    pos[id] = (x, y)
    board_map[pos[id][0]][pos[id][1]] = id
    is_live[id] = True
    
for t in range(1, m+1):
    cloX, cloY, cloIdx = 10000, 10000, 0
    
    for i in range(1, p+1):
        if not is_live[i]:
            continue
        
        currentBest = ((cloX - rudolf[0]) ** 2 + (cloY - rudolf[1]) ** 2, (-cloX, -cloY))
        currentValue = ((pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2, (-pos[i][0], -pos[i][1]))
        
        if currentValue < currentBest:
            cloX, cloY = pos[i]
            cloIdx = i
    
    if cloIdx:
        prevRudolf = rudolf
        moveX = 0
        if cloX > rudolf[0]:
            moveX = 1
        elif cloY < rudolf[1]:
            moveY = -1
            
        rudolf = (rudolf[0] + moveX, rudolf[1] + moveY)
        board_map[prevRudolf[0]][prevRudolf[1]] = 0
    
    # rudolf 충돌
    if rudolf[0] == cloX and rudolf[1] == cloY:
        firstX = cloX + moveX * c
        firstY = cloY + moveY * c
        lastX, lastY = firstX, firstY
        
        stun[cloIdx] = t + 1
        
        while is_inrange(lastX, lastY) and board_map[lastX][lastY] > 0:
            lastX += moveX
            lastY += moveY
            
        while not (lastX == firstX and lastY == firstY):
            beforeX = lastX - moveX
            beforeY = lastY - moveY
            
            idx = board_map[beforeX][beforeY]
            
            if not is_inrange(lastX, lastY):
                is_live[idx] = False
            else:
                board_map[lastX][lastY] = board_map[beforeX][beforeY]
                pos[idx] = (lastX, lastY)
            
            lastX, lastY = beforeX, beforeY
            
        points[cloIdx] += c
        pos[cloIdx] = (firstX, firstY)
        if is_inrange(firstX, firstY):
            board_map[firstX][firstY] = cloIdx
        else:
            is_live[cloIdx] = False
            
    board_map[rudolf[0]][rudolf[1]] = -1
    
    for i in range(1, p+1):
        if not is_live[i] or stun[i] >= t:
            continue
    
        minDist = (pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2
        moveDir = -1
        
        for dir in range(4):
            nx = pos[i][0] + dx[dir]
            ny = pos[i][1] + dy[dir]
            
            if not is_inrange(nx, ny) or board_map[nx][ny] > 0:
                continue
            dist = (nx - rudolf[0]) ** 2 + (ny - rudolf[1]) ** 2
            if dist < minDist:
                minDist = dist
                moveDir = dir
            
            if moveDir != -1:
                nx = pos[i][0] + dx[moveDir]
                ny = pos[i][1] + dy[moveDir]
                
                if nx == rudolf[0] and ny == rudolf[1]:
                    stun[i] = t + 1
                    
                    moveX = -dx[moveDir]
                    moveY = -dy[moveDir]
                    
                    firstX = nx + moveX * d
                    firstY = ny + moveY * d
                    lastX, lastY = firstX, firstY
                    
                    if d == 1:
                        points[i] += d
                    else:
                        while is_inrange(lastX, lastY) and board_map[lastX][lastY] > 0:
                        lastX += moveX
                        lastY += moveY

                    # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
                    # 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not is_inrange(beforeX, beforeY):
                            break

                        idx = board_map[beforeX][beforeY]

                        if not is_inrange(lastX, lastY):
                            is_live[idx] = False
                        else:
                            board_map[lastX][lastY] = board_map[beforeX][beforeY]
                            pos[idx] = (lastX, lastY)

                        lastX, lastY = beforeX, beforeY

                    points[i] += d
                    board_map[pos[i][0]][pos[i][1]] = 0
                    pos[i] = (firstX, firstY)
                    if is_inrange(firstX, firstY):
                        board_map[firstX][firstY] = i
                    else:
                        is_live[i] = False
            else:
                board_map[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nx, ny)
                board_map[nx][ny] = i

    # 라운드가 끝나고 탈락하지 않은 산타들의 점수를 1 증가시킵니다.
    for i in range(1, p+1):
        if is_live[i]:
            points[i] += 1


# 결과를 출력합니다.
for i in range(1, p + 1):
    print(points[i], end=" ")