N, K = map(int, input().split())
      
n_list = [False] * (N + 1)
cnt = 0
for i in range(2, N+1):
    if n_list[i] == False:
        for j in range(i, N+1, i): # 배수 표현할 때 이렇게 써도 될 듯?
            if n_list[j] == False:
                n_list[j] = True
                cnt += 1
                if cnt == K:
                    print(j)


