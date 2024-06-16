N, K = map(int, input().split())

# N은 얼음 양동이의 개수
# K는 팔 뻗을 수 있는 길이 
# x는 위치 g는 얼음 개수 생각하면 편함



ice_info_list = [tuple(map(int, input().split())) for _ in range(N)]

ice_info_list.sort(key = lambda x: x[1])

# (5,1), (2,2), (4,7), (10,15)
# 일단 좌표에 대입을 다 하면?


left_max = 0
right_max = 0
ice_sum_max = 0
while True:
    for ice_info in ice_info_list:
        a_x = ice_info[1]
        a_g = ice_info[0]

        left_max = a