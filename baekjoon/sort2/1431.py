N = int(input())
# def sum_sum(inputs):
#     result = 0
#     for i in inputs:
#         if i.isdigit():
#             result += int(i)
#     return result
#
# str_list = [input() for _ in range(N)]
# str_list.sort(key = lambda x: (len(x), sum_sum(x), x))
# for i in str_list:
#     print(i)

for _ in range(N):



str_list = [(s, sum(int(ch) for ch in s if ch.isdigit())) for s in (input() for _ in range(N))]
str_list.sort(key = lambda x: (len(x[0]), x[1], x[0]))
for s, _ in str_list:
    print(s)