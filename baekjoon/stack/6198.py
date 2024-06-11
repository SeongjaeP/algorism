from collections import deque

n = int(input())
building_list = list(int(input()) for _ in range(n))
stack = []
answer = 0 

for i in range(n):
    while stack and stack[-1] <= building_list[i]:
        stack.pop()
    stack.append(building_list[i])
    answer += len(stack) - 1

print(answer)
    


