input_data = input()
row = int(input_data)
column = int(ord(input_data[0])) - int(ord('a')) + 1

directions = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]

result = 0
for direction in directions:
    next_row = row + direction[0]
    nex_column = column + direction[1]

    if next_row >= 1 and next_row <= 8 and nex_column >= 1 and nex_column <= 8:
        result += 1


print(result)