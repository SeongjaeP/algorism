S = input()

result = int(S[0])

for i in range(1, len(S)):
    k = int(S[i])
    if k <= 1 or result <= 1:
        result += k    
    else:
        result *= k
print(result)



# for i, k in enumerate(S):
# #for i in range(1, len(S)):
#     k = int(S[i])
#     if k <= 1 or result <= 1:
#         result += k
    
#     else:
#         result *= k

# print(result)

     
