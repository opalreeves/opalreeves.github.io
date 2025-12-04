def dot_product(a, b):
    if len(a) != len(b):
        return None
    
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total

def matrix_mult(A, B):
    if len(A[0]) != len(B):
        return None
    
    result = []

    num_rows_A = len(A)
    num_columns_B = len(B[0])

    for i in range(num_rows_A):
        new_row = []
        
        for j in range(num_colums_B):
            column = []
            
            for k in range(len(B)):
                column.append(B[k][j])

            value = dot_product(A[i], column)
            new_row.append(value)

        result.append(new_row)
    return result


