# X // 3 == 0  X / 3
# X // 2 == 0 X / 2
# X - 1 

N = int(input())
dp = [0] * 10^6
pre_dp = [0] * 10^6

def calculate(X):
    if X // 3 == 0:
        X = X / 3

    if X // 2 == 0:
        X = X / 2


