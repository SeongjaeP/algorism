char_list = [input().strip() for _ in range(5)]
result = []
N = len(max(char_list, key = len))

for i in range(N):
    for j in range(5):
        if i < len(char_list[j]):
            result.append(char_list[j][i])

print(''.join(result))
