def find_thue_morse(k):
    if k == 0:
        return 0
    return 1 - find_thue_morse(k - 2**(k.bit_length() - 1))


k = int(input()) - 1 
print(find_thue_morse(k))



# 50번만 반복해도 문자열의 길이가 2^50이니 ,, 너무 커서 
# 해당 위치의 문자가 원래 0인지 1인지 판단하면 됨