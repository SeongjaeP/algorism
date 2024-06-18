S = input()
S_len = len(S)

## method 1

left = 0
right = 1
result = []

while left <= S_len-1:
    if left != right:
        result.append(S[left:right])
    if right == S_len:
        left += 1
        right = left + 1
        continue  
    right += 1

print(len(set(result)))

### method 2. 
unique_substrings = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        unique_substrings.add(S[i:j])

print(len(unique_substrings))

