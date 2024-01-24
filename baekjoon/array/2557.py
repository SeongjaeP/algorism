#method 1

# A = int(input())
# B = int(input())
# C = int(input())
#
# D = A * B * C
# res = [int(x) for x in str(D)]
#
# lst = [0] * 10
# for i, cnt in enumerate(lst):
#     for j in res:
#         if i == j:
#             cnt += 1
#     print(cnt)
#
#
# # method2
#
# result = list(str(A*B*C))
#
# for i in range(10):
#     print(result.count(str(i)))
#

# method3 efficiently version

# Initialize a list of 10 zeros for counting each digit (0 through 9)

A = int(input())
B = int(input())
C = int(input())

D = A * B * C

lst = [0] * 10
res = [int(x) for x in str(D)]
# Count the frequency of each digit
for digit in res:
    lst[digit] += 1

# Print the count of each digit
for count in lst:
    print(count)