# Method1

N = int(input())
for i in range(1, N+1):
    print('{}{}{}'.format('*'* i, ' '* (2*(N-i)), '*' * i))


for i in range(N-1, 0 , -1):
    #print(i)
    print('{}{}{}'.format('*'* i,' '* (2 * (N-i)), '*' * i))



