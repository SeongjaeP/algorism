#

# 1~ N이 있는데 
# nCm 
# 적어도 k개가 같으면 당첨 
# -> 아예 다르거나 k-1개가 같은 경우 

from itertools import combinations
import math
n, m, k = map(int,input().split())

a = math.comb(m,k)
b = math.comb(n,m)



print(1 - a/b)