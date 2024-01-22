N = int(input())

# input().split()으로 입력을 받고, 그 결과를 map으로 감싼 다음에 tuple로 변환
input_list = [tuple(map(int, input().split()[1:])) for i in range(N)]
print(input_list)