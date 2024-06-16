# E는 x+1
# W는 x-1

n = int(input())
# EW 붙으면 
strings =input()
len_str = len(strings)
cnt = 0
for i in range(len_str - 1):
    
    if strings[i] == 'E':
        if strings[i+1] == 'W':
            cnt += 1


print(cnt)         
    
