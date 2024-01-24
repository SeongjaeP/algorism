def sorting(lst):
    lst = list(dict.fromkeys(lst))
    lst.sort(key=lambda x: (len(x), x))
    return lst

N = int(input())
input_list = list(input() for _ in range(N))
sorted_list = sorting(input_list)
print(*sorted_list, sep='\n')



