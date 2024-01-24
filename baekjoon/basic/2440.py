N = int(input())
for i in range(N):
    result = '{0:<5}'.format('*' *(N-i))
    print(result)