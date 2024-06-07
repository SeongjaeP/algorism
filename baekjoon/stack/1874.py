n = int(input())

num_list = list(map(int, input().split()) for _ in range(n))

cnt = 1
stack = []
tmp = []

for i in range(n):
    
# 4 3 6 8 7 5 2 1

# 1 2 3 4 + + + +
# 4 3 - -

# 1 2 5 6 + + 
# 4 3 6 -

# 1 2 5 7 8 + +
# 4 3 6 8 7 - -

# 1 2 5 - - -
# 4 3 6 8 7 5 2 1

