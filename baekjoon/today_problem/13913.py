a = 'bar'

b = 'bsdfagwgr'

for i in range(len(b) - len(a) + 1):
    interval = b.find(a[1], i) - b.find(a[0], i)
    print(a[1])
    print(i)
    print(b.find(a[1],i))
    