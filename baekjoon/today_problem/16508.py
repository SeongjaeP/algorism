S = input().strip()
N = int(input())

book_set = [tuple(input().split()) for _ in range(N)]

book_set.sort(key = lambda x: x[0])

for book_info in book_set:

    print(book_info[0])
    # 하나씩 털면서 S의 단어가 있는지 확인하고 있으면 추가하는식으로



target = input().strip()
N = int(input())

prices = []
for n in range(N):
    price, title = map(str, input().strip().split())
    prices.append([int(price), Counter(title)])
result = float('inf')

for i in range(1<<N):
    price = 0
    alpha = Counter()
    for j in range(N):
        if (i)


# ALMIGHTY이면 
#


# 35000 COMPUTERARCHITECTURE
# 40000 OPERATINGSYSTEM
# 43000 NETWORK
# 47000 ALGORITHM
# 문자열을 정렬해야할듯?