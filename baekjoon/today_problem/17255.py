def dfs(string):
    global cnt
    if len(n) == 1:
        cnt +=1
        return
    L = set(list(string))
    if len(L) == 1:
        cnt+=1
        return
    else:
        dfs(string[1:])
        dfs(string[:-1])

n = input()
cnt = 0
dfs(n)
print(cnt)




def dfs(string):
    global cnt
    if len(n) == 1:
        cnt += 1
        return
    L = set(list(string))
    if len(L) == 1:
        cnt += 1
        return
    else:
        dfs(string[1:])
        dfs(string[:-1])

        