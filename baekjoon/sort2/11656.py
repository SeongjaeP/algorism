s = input()

answer = [s[i:] for i in range(len(s))]
answer.sort()

for suffix in answer:
    print(suffix)