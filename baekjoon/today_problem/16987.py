def break_eggs(index, eggs, broken_count):
    if index == len(eggs):
        return broken_count
    
    if eggs[index][0] <= 0:
        return break_eggs(index + 1, eggs, broken_count)
    
    all_broken = broken_count
    hit_any = False

    for i in range(len(eggs)):
        if i != index and eggs[i][0] > 0:
            hit_any = True

            # 서로 쳐야함
            eggs[index][0] -= eggs[i][1]
            eggs[i][0] -= eggs[index][1]

            # 깨졌는지 확인
            current_broken = broken_count
            if eggs[index][0] <= 0:
                current_broken += 1
            if eggs[i][0] <= 0:
                current_broken += 1


            all_broken = max(all_broken, break_eggs(index + 1, eggs, current_broken))

            # 되돌리기
            eggs[index][0] += eggs[i][1]
            eggs[i][0] += eggs[index][1]


    if not hit_any:
        all_broken = max(all_broken, break_eggs(index + 1, eggs, broken_count))

    return all_broken

N = int(input())
egg_list = [list(map(int, input().split())) for _ in range(N)]
print(break_eggs(0, egg_list, 0))
