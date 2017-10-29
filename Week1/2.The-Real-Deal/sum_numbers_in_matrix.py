def sum_matrix(matrix):
    return sum([sum(single_matrix) for single_matrix in matrix])

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m))
m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))
