def is_valid_sign(shop_name, sign):
    shop_len = len(shop_name)
    sign_len = len(sign)


    for i in range(sign_len):
        if sign[i] == shop_name[0]:
            j = 1
            gap = 0

            while j < shop_len:
                k = i + j * gap
                if k >= sign_len:
                    break
                if sign[k] == shop_name[j]:
                    j += 1
                else:
                    if gap == 0:
                        gap = k - i
                    
                    else:
                        break
            if j == shop_len:
                return True
    return False


n = int(input())
shop_name = input().strip()
old_signs = [input().strip() for _ in range(n)]

result = 0
for sign in old_signs:
    if is_valid_sign(shop_name, sign):
        result += 1

print(result)


### gpt센세,,, 

def is_valid_sign(shop_name, sign):
    shop_len = len(shop_name)
    sign_len = len(sign)
    
    # 가능한 모든 시작 위치에서 shop_name의 첫 문자가 매칭되는지 확인
    for i in range(sign_len):
        if sign[i] == shop_name[0]:
            for gap in range(1, sign_len):
                valid = True
                for j in range(1, shop_len):
                    k = i + j * gap
                    if k >= sign_len or sign[k] != shop_name[j]:
                        valid = False
                        break
                if valid:
                    return True
    return False

# 입력 받기
n = int(input())
shop_name = input().strip()
old_signs = [input().strip() for _ in range(n)]

# 결과 계산
result = 0
for sign in old_signs:
    if is_valid_sign(shop_name, sign):
        result += 1

print(result)
