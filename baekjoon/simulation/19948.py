# texts = input().split()
# N = int(input())
# alp_cnt = list(map(int, input().split()))

# capitals = ''.join([word[0] for word in texts.split()])
# tmp_str = ''
# recordable = True

# for c in capitals:
#     if tmp_str == c:
#         continue
#     tmp_str = c
#     k = ord(c.lower()) - ord('a')
#     if alp_cnt[k] > 0:
#         alp_cnt[k] -= 1
#     else:
#         recordable = False

# tmp_str = ''
# for c in texts:
#     if tmp_str == c:
#         continue
#     tmp_str = c
#     if c.isalpha():
#         k = ord(c.lower()) - ord('a')
#         if alp_cnt[k] > 0:
#             alp_cnt[k] -= 1
#         else:
#             recordable = False
        
#     else:
#         if N > 0:
#             N -= 1
#         else:
#             recordable = False

# print(capitals.upper() if recordable else -1)




texts = input().split()
N = int(input())  # 공백(또는 기타 문자) 사용 가능 횟수
alp_cnt = list(map(int, input().split()))

capitals = ''.join(word[0] for word in texts)  # 각 단어의 첫 글자만 사용
recordable = True

for c in capitals:
    k = ord(c.lower()) - ord('a')
    if alp_cnt[k] > 0:
        alp_cnt[k] -= 1
    else:
        recordable = False
        break

if recordable:
    for i, word in enumerate(texts):
        
        for c in word:
            k = ord(c.lower()) - ord('a')
            if alp_cnt[k] > 0:
                alp_cnt[k] -= 1
            else:
                recordable = False
                break
        if not recordable:
            break

       
        if i > 0:
            if N > 0:
                N -= 1
            else:
                recordable = False
                break

print(capitals.upper() if recordable else -1)

# 중복되는 경우 고려 안했음.