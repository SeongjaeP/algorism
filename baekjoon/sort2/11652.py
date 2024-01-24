
# 정렬로 시간 줄이기, Counter는 dictionary느낌으로 접근하면 아주 좋음

from collections import Counter
import sys

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
num_counts = Counter(num_list)

max_count = num_counts.most_common(1)[0][1]

most_frequent = min(k for k, v in num_counts.items() if v == max_count)

print(most_frequent)


sorted_counts = sorted(num_counts.items(), key=lambda x: x[1], reverse=True)
print(sorted_counts[0][0])



# 정렬로 시간 줄이기, Counter는 dictionary느낌으로 접근하면 아주 좋음