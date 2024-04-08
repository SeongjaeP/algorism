N = int(input())

# 00 00 00 
result = 0
for i in (0, N + 1):
    for j in (0, 60):
        for k in (0, 60):
    #         k.split()
    #         if k in '3':
    #             result += 1
    #     j.split()
    #     if j in '3':
    #         result += 1
    # i.split()
    # if i in '3':
    #     result += 1


            if '3' in str(i) + str(j) + str(k):
                result +=1
print(result)