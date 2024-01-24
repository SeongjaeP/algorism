# method1
from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
alpha_dict = {}

for i in ascii_lowercase:
    alpha_dict[i] = 0

S = list(input())
for i in S:
    if i in alpha_dict:
        alpha_dict[i] += 1

for k, v in alpha_dict.items():
    print(v, end = ' ')

# method2

alnum = [0]*26
for i in input():
    alnum[ord(i)-97] += 1
print(*alnum)