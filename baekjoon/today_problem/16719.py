a = input()

character_list = list(a)
character_list.sort()

result = []
for i in character_list:
    result.append(i)
    print(''.join(result))

