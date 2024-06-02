import math

res = [int(x) for x in str(input())]

lst = [0] * 10
for i in res:
    lst[i] += 1

# 6과 9를 숫자를 카운트해서 2로 나누어 떨어지면 그 값으로 하기
cnt = lst[6] + lst[9]
lst[6] = lst[9] = math.ceil(cnt / 2)
print(max(lst))