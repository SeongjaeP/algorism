# 순서
T = int(input())

for _ in range(T):
    word = list(input().strip())
    n = len(word)

    i = n - 1
    while i > 0 and word[i] <= word[i - 1]:
        i -= 1

    if i <= 0:
        print("".join(word))
        continue

    j = n - 1
    while word[j] <= word[i - 1]:
        j -= 1

    word[i - 1], word[j] = word[j], word[i - 1]
    word[i:] = sorted(word[i:])

    print("".join(word))
    # 리스트를 문자열로 변환하여



# 7 4 11 11 14 -> 7 4 11 14 11

# 7 4 14 11 11 -> 7 14 4 11 11 
    
    
    
    
# HELLO -> HELOL
# DRINK -> 
# 알파벳을 나타내는 index로 바꾸고 여기서 