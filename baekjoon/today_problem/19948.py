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
        prev_char = None  
        for c in word:
            k = ord(c.lower()) - ord('a')
            
            if c != prev_char: 
                if alp_cnt[k] > 0:
                    alp_cnt[k] -= 1  
                else:
                    recordable = False
                    break  
            prev_char = c  
            
        if not recordable:
            break

        if i > 0:  
            if N > 0:
                N -= 1  
            else:
                recordable = False
                break

print(capitals.upper() if recordable else -1)