def add(*matrices):
    result = []
    for matrix in matrices:
        result.append([])
        for row in matrix:
            columns = []
            sums = []
            for column in row:
                columns.append(column)
            if len(columns) != len(row):
                raise ValueError("Matrices are not the same size.")
            sums.append(sum(columns))

    outer_list = []
    for o1, o2 in zip(matrix1, matrix2):
        inner_list = []
        for i1, i2 in zip(o1, o2):
            inner_list.append(i1 + i2)
        outer_list.append(inner_list)
    return outer_list


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add(matrix1, matrix2))

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2))
