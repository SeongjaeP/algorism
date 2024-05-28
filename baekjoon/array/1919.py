# 두 입력을 sort해서 정렬해서 인덱스가 다른 게 있으면 결과값에 +1하면서 진행
# 인덱스로 하면 안됨

# A = str(input())
# B = str(input())
#
# A_lst = list(A)
# B_lst = list(B)
#
# intersection = set(A_lst) & set(B_lst)
#
# A_lst = [item for item in A_lst if item not in intersection]
# B_lst = [item for item in B_lst if item not in intersection]
#
# print(len(A_lst) + len(B_lst))


# A = list(input())
# B = list(input())
#
# rst_A = [x for x in A if not x in B or B.remove((x))]
# rst_B = [x for x in A if not x in A or A.remove((x))]
#
# print(len(rst_A) + len(rst_B))

# Counter쓰면 간단하네여 ^^
from collections import Counter

str1 = input()
str2 = input()

count_str1 = Counter(str1)
count_str2 = Counter(str2)

total_to_remove = sum((count_str1 - count_str2).values()) + sum((count_str2 - count_str1).values())

print(total_to_remove)