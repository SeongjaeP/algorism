import random

num_list = list(int(input()) for _ in range(9))
while True:
    sample_list = random.sample(num_list, 7)
    if sum(sample_list) == 100:
        sample_list.sort()
        for num in sample_list:
            print(num)
        break