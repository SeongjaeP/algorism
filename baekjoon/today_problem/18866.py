# 5
# 5 1
# 4 2
# 3 3
# 2 5
# 1 4

# 임의의 젊은 날의 행복도는 임의의 늙은 날의 행복도보다 높다.
# 임의의 젊은 날의 피로도는 임의의 늙은 날의 피로도보다 낮다.


n = int(input())
mind_list = [tuple(map(int,input().split())) for _ in range(n)]
mind_list.sort(key = lambda x: -x[0])

print(mind_list)


for 



