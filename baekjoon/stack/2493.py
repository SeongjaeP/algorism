# 꼭대기에 수신기 설치


# 6 9 5 7 4
# 4 -> 7 -> 9 -> 

n = int(input())
tower_list = list(map(int,input().split()))
answer = [0] * n
stack = []


for i in range(n):
    while stack and tower_list[stack[-1]] < tower_list[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(map(str, answer)))