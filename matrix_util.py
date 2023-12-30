#
# MATRIX MULTIPLICATION UTILS
#

# ------------------------------ product of two matrices -----------------------------
def matrix_product(m1, m2):
    if not equal_rows(m1) or not equal_rows(m2):
        print("matrix input incorrect")
        return

    if not cols_rows_match(m1, m2):
        print("number of columns of the first matrix must match the number of rows of the second matrix")
        return

    output = []

    columns = len(m2[0])
    rows = len(m1)

    for m in range(rows):
        output_row = []
        for n in range(columns):
            output_row.append(vector_dot_product(m1[m], extract_column(m2, n)))
        output.append(output_row)

    return output


# ---------------------------- dot product of two vectors ----------------------------
def vector_dot_product(v1, v2):
    if len(v1) != len(v2):
        print("vectors must be equal in length")
        return

    output = 0
    for i in range(len(v1)):
        output += v1[i] * v2[i]
    return output


# --------------------------- vector product with a scalar ---------------------------
def vector_scalar_product(vector, scalar):
    output = []

    for i in range(len(vector)):
        output.append(vector[i] * scalar)

    return output


# --------------------------- matrix product with a scalar ---------------------------
def matrix_scalar_product(matrix, scalar):
    output = []

    for i in range(len(matrix)):
        output.append(vector_scalar_product(matrix[i], scalar))

    return output


# -------------------------- extract matrix column to vector -------------------------
def extract_column(matrix, column_index):
    column = []
    for row in matrix:
        column.append(row[column_index])
    return column


# -------------------- check if given list of lists forms a matrix -------------------
def equal_rows(matrix):
    columns = len(matrix[0])
    for m in matrix:
        if len(m) != columns:
            print("matrix lists must be equal in length")
            return False
    return True


# -- check if nr of cols of the first matrix equals nr of rows of the second matrix --
def cols_rows_match(m1, m2):
    return len(m1[0]) == len(m2)
