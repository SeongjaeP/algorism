from collections import Counter

N, C = map(int, input().split())
num_list = list(map(int, input().split()))

# 빈도 계산 더 깔끔
sorted_list =Counter(num_list).most_common()
print(sorted_list)

for x, y in sorted_list:
    print(x,y)
    for _ in range(y):
        print(x, end=' ')