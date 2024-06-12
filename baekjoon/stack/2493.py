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

# i = 0
# False -> False stack.append(0)
# i = 1
# stack = [0] and tower_list[0] < tower[1] = 9 
# stack.pop() -> stack = []
# stack = [1] 
# tower_list[1] = 9 < tower_list[2] = 5: 거짓 
# stack = [1]
# answer[2] = 1 + 1
# stack = [1, 2]

# i = 3
# while 5 < 7
# stack.pop() -> stack = [1]
# answer[3] = 2
# stack = [1, 3]

# i = 4
# while 7 < 

print(' '.join(map(str, answer)))