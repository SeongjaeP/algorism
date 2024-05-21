start_keys = input()
typing_string = input()
left_start, right_start = start_keys.split()

left_keys = set("qwertasdfgzxcv")
right_keys = set("yuiophjklbnm")

keyboard_layout = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

keyboard = {ch: (i, j) for i, row in enumerate(keyboard_layout) for j, ch in enumerate(row)}

def manhattan_distance(key1, key2):
    x1, y1 = keyboard[key1]
    x2, y2 = keyboard[key2]
    return abs(x1 - x2) + abs(y1 - y2)


total_time = 0

for char in typing_string:
    if char in left_keys:
        move_time = manhattan_distance(left_start, char)
        total_time += move_time + 1
        left_start = char
    else:
        move_time = manhattan_distance(right_start, char)
        total_time += move_time + 1
        right_start = char

print(total_time)