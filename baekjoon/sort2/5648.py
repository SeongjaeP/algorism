N, *S = input().split()
while len(S) < int(N):
    data = input().split()
    S.extend(data)
answer = [int(element[::-1]) for element in S]
answer.sort()
print(*answer, sep='\n')



