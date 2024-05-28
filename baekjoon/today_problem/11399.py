# 3 1 4 3 2
# 1 2 3
# 1 2 3 4 5


# 1  # > 1
# 1 2 > 3
# 1 2 3 # > 6
# 1 2 3 4  > 10 
# 1 2 3 4 5  > 15


n = int(input())

num_list = list(map(int, input().split()))
num_list.sort()

result = []
cnt = 0

# method 1
for i in num_list:
    cnt += i
    result.append(cnt)

# method 2
for i in num_list:
    cnt += sum(num_list[0:i])

print(sum(result))



        # 1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 3, 1 + 2 + 3 + 3 + 4 
        # 1, 3, 6, 9, 13



#