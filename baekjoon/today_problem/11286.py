import heapq
import sys

input = sys.stdin.readline
n = int(input().strip())  # 첫 번째 줄에서 n을 읽고 양 끝 공백 제거
heap = []

for _ in range(n):
    num = int(input().strip())  # 각 입력에서 숫자를 읽고 양 끝 공백 제거
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)