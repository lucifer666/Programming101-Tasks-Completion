#refactoring needed


def magic_square(matrix):
    return rows_sum(matrix) == cols_sum(matrix) == main_diagonal_sum(matrix) == antidiagonal_sum(matrix)


def rows_sum(matrix):
    single_row_sum = sum(matrix[0])
    for row in matrix:
        if single_row_sum != sum(row):
            return False
    return single_row_sum

def cols_sum(matrix):
    transposed_matrix = []
    for row in range(0, len(matrix)):
        inner_matrix = []
        for col in range(0, len(matrix)):
           inner_matrix.append(matrix[col][row])
           if col == len(matrix)-1:
               transposed_matrix.append(inner_matrix)
    single_col_sum = sum(transposed_matrix[0])
    for row in transposed_matrix:
        if single_col_sum != sum(row):
            return False
    return single_col_sum

def main_diagonal_sum(matrix):
    return sum([matrix[index][index] for index in range(0, len(matrix))])

def antidiagonal_sum(matrix):
    row = 0
    col = len(matrix) - 1
    sum = 0
    while(col != -1):
        sum += matrix[row][col]
        row += 1
        col -= 1
    return sum








print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print(magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
