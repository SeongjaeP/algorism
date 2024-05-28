N = int(input())
for i in range(N, 0 , -1):
    #print(i)
    print('{}{}'.format(' '* (N-i),'*'* (2*i - 1)))