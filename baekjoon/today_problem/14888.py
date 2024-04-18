# 차례대로 덧셈 뺄셈 곱셈 나눗셈
# 순서대로 '+', '-', '*', '//'

n = int(input())
integer = list(map(int ,input().split()))
add, sub, mul, div = map(int, input().split())
# [ '+', '-', '*', '//']
min_value = 1e9
max_value = -1e9


# 전부다 확인 해야함. >> dfs와 백트래킹을 이용하면 될듯?
def dfs(i, result, add, sub, mul, div):
    global max_value, min_value


    if i == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if add:
        dfs(i + 1, result + integer[i], add - 1, sub, mul, div)
    if sub:
        dfs(i + 1, result - integer[i], add, sub - 1, mul, div)
    if mul:
        dfs(i + 1, (result * integer[i]), add, sub, mul - 1, div)
    if div:
        if result < 0:
            dfs(i + 1, -(-result // integer[i]), add, sub, mul, div - 1)
        else:
            dfs(i + 1, (result // integer[i]), add, sub, mul, div - 1)


# 첫 번째 숫자와 연산자를 이용해 dfs 시작
dfs(1, integer[0], add, sub, mul, div)

# 결과 출력 int로 출력해야 에러가 안 뜸
print(int(max_value))
print(int(min_value))

