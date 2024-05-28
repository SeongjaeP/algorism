# Method1
N = int(input())
for i in range(N, 0 , -1):
    print('{}{}'.format(' '* (N-i),'*'* (2*i-1)))


for i in range(1, N):
    print('{}{}'.format(' '* (N-i-1),'*'* (2*i+1)))






