# X의 수가 O보다 크거나 같아야함.
# 그러니 입력을 다 받고 x_cnt와 o_cnt의 수를 세줘야함.

x_cnt = 0
o_cnt = 0 

if x_cnt >= o_cnt:
    



else:
    print('INVALID')



while True:
    board = input()
    if board == "end":
        break
    else:
        x_cnt = 0
        o_cnt = 0 
        arr = [[0]*3 for _ in range(3)]
        for i in range(3):
            