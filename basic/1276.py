# method1)
N = int(input())
call_list = list(map(int, input().split()))

result1 = 0  # 영식 요금제
result2 = 0  # 민식 요금제

for i in call_list:
    result1 += (i // 30 + 1) * 10

for j in call_list:
    result2 += (j // 60 + 1) * 15

final_result1 = ['Y', result1]
final_result2 = ['M', result2]
equal = ['Y', 'M', result1]

if result1 > result2:
    print(' '.join(map(str, final_result2)))

elif result1 < result2:
    print(' '.join(map(str, final_result1)))

else:
    print(' '.join(map(str, equal)))

# method2) using function

def calculate_fee(call_time, fee_per_period, period):
    return (call_time // period + 1) * fee_per_period

N = int(input())
call_list = list(map(int, input().split()))

young_fee = sum(calculate_fee(time, 10, 30) for time in call_list)
min_fee = sum(calculate_fee(time, 15, 60) for time in call_list)

if young_fee < min_fee:
    print(f'Y {young_fee}')
elif young_fee > min_fee:
    print(f'M {min_fee}')
else:
    print(f'Y M {young_fee}')