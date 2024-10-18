n, m = map(int,input().split())
num_list = list(map(int,input().split()))

start = 0
end = 0
count_odd = 0
max_length = 0

# 1 3 4 6 7 8 9 

# start를 짝수로
while end < n:
    if num_list[end] % 2 == 0:
        end += 1
    else:
        if count_odd < m:
            count_odd += 1
            end += 1
        else:
            if num_list[start] % 2 != 0:
                count_odd -= 1
            start += 1
            
    max_length = max(max_length, end - start - count_odd)

print(max_length)