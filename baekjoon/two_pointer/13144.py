# from collections import deque
N = int(input())

num_list = list(map(int, input().split()))

# queue = deque()

left = 0
right = 0
unique_set = set()
cnt = 0

# right가 N에 도달하면 left를 + 1 해서 다시 시작. while 문을 끝내는 지점은 left가 N일 때
while right < N:
    if num_list[right] not in unique_set:
        unique_set.add(num_list[right])
        cnt += right - left + 1
        right += 1

    else:
        unique_set.remove(num_list[left])
        left += 1

print(cnt)



from collections import deque
