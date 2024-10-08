# 5
# 55 185
# 58 183
# 88 186
# 60 200
# 46 155

N = int(input())
hu_list = [tuple(map(int, input().split())) for _ in range(N)]
#hu_list.sort(key = lambda x: -x[0])


# 내 생각엔
# 기준을 하나만 잡고 내림차순하고
# 

for i in hu_list:
    rank = 1
    for j in hu_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")
    