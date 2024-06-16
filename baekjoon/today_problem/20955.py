N, M = map(int, input().split())


parent = list(range(N+1))

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    if find_parent(parent, u) == find_parent(parent, v):
        cnt += 1
    union_parent(parent, u, v)

link=0
for i in range(1,N):
    if find_parent(parent,i)!=find_parent(parent,i+1):
        union_parent(parent,i,i+1)
        link+=1
 
print(cnt+link)