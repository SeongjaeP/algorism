import sys

N = int(sys.stdin.readline().strip())
num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

num_list.sort(reverse=True)


for i in num_list:
    print(i)

# 출력 부분 최적화
sys.stdout.write('\n'.join(map(str, num_list)))