n = int(input())

stack = []
answer = []
flag = 0
cur = 1

for _ in range(n):
    num = int(input())
    while cur <= num: # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append('+')
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉 cur == num일 때 까지 while문을 돌아 스택을 쌓음.

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
    

