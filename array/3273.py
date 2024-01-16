# method 1 O(N^2) 시간초과 발생
# N = int(input())
# num_list = list(map(int, input().split()))
# x = int(input())
#
# rst = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if num_list[i] + num_list[j] == x:
#             rst += 1
# print(rst)


# method2
N = int(input())
num_list = list(map(int, input().split()))
x = int(input())

num_dict = {}
rst = 0
for num in num_list:
    if x - num in num_dict:
        rst += 1
    num_dict[num] = True
    print(num_dict)
print(rst)

