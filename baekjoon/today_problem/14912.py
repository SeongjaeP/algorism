n, d = map(int, input().split())
count = 0


for number in range(1, n+1):
    number_str = str(number)
    count += number_str.count(str(d))
    
print(count)
