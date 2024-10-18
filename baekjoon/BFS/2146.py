# 10
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 0 0 0 0 1 1
# 1 0 1 1 0 0 0 0 1 1
# 0 0 1 1 1 0 0 0 0 1
# 0 0 0 1 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
# 각각의 맵을 큐로 


# 0을 2로 바꾸면서 

def bfs(x,y,label):
    queue = deque([(x,y)])
    visited[x][y] = True
    map_list[x][y] = label
    island_queue.append((x,y))
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and map_list[nx][ny] == 1:
                visited[nx][ny] = True
                map_list[nx][ny] = label
                queue.append((nx, ny))
                island_queue.append((nx,ny))
 
 
                
def shortest_dist(v):
    
    distance_queue = deque(island_queue)
    distance = [[-1] * n for _ in range(n)]
    
    for x,y in island_queue:
        distance[x][y] = 0
        
    min_dist = float('inf')
    
    while distance_queue:
        x, y = distance_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if map_list[nx][ny] == 0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    distance_queue.append((nx, ny))
                    
                elif map_list[nx][ny] != map_list[x][y] and map_list[nx][ny] != 0:
                    min_dist = min(min_dist, distance[x][y])
                    
                    
    return min_dist
        
    
n = int(input())
map_list = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
island_queue = deque()

label = 2
for i in range(n):
    for j in range(n):
        if map_list[i][j] == 1 and not visited[i][j]:
            bfs(i,j,label)
            label += 1
            
            

res = float('inf')
for v in range(1, label):
    res = min(res, shortest_dist())
print(res)
