num_list = [list(map(int,input().split())) for _ in range(3)]

# 0의 개수로 dict
dict1 = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E'}
for i in num_list:
    count_zero = i.count(0)
    print(dict1[count_zero])