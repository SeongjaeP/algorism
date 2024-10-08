from collections import Counter

matrix = [[3,1,2],
          [1,1,2],
          [5,5,5]]

#sorted(ex_counter.items(), key=lambda x: -x[1])


# row 작업완료 

def based_row(matrix):
    
    new_matrix = []
    for row in matrix:
        
        new_row = []
        ex_counter = Counter(row)
        sorted_counter = sorted(ex_counter.items(), key=lambda x: (-x[1], x[0]))
        for item, count in sorted_counter:
            new_row.extend([item, count])
        new_matrix.append(new_row)
            
    lengths = [len(row) for row in new_matrix]
    max_length = max(lengths)
    for row in new_matrix:
        while len(row) < max_length:
            row.append(0)
        
    return new_matrix


def based_column(matrix):
    
    columns = [ [row[i] for row in matrix] for i in range(len(matrix[0]))]
    new_columns = []

    for col in columns:
        ex_counter = Counter(col)
        sorted_counter = sorted(ex_counter.items(), key=lambda x: (-x[1], x[0]))
        new_col = []
        for item, count in sorted_counter:
            new_col.extend([item, count])
        new_columns.append(new_col)

    max_length = max(len(col) for col in new_columns)

    for col in new_columns:
        while len(col) < max_length:
            col.append(0)
    
    transposed_columns_matrix = list(zip(*new_columns))
    
    return transposed_columns_matrix