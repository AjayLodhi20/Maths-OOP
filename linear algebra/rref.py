def compute_rref(matrix):
    A = [row[:] for row in matrix]

    rows = len(A)
    cols = len(A[0]) if rows > 0 else 0
    pivot_row = 0


    for col in range(cols)
