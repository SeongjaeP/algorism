N = int(input())
for i in range(N):
    #print('{:>5}'.format('*' *(N-i), N))
    print('{}{}'.format(' '* i ,'*'*(N-i)))