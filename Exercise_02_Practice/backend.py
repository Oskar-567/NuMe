import numpy as np

# Task a)
# Implement a method, calculating the LU factorization of A.
# Input: Matrix A - 2D numpy array (e.g. np.array([[1,2],[3,4]]))
# Output: Matrices P, L and U - same shape as A each.
def lu(A):
    A = A.astype(float)
    U = A.copy()
    n, m = A.shape
    L = np.eye(n)
    P = np.eye(n)

    for k in range(m-1):
        max_row = np.argmax(np.abs(U[k:, k])) + k
        if max_row != k:
            U[[k, max_row], :] = U[[max_row, k], :]
            P[[k, max_row], :] = P[[max_row, k], :]
            if k >= 1:
                L[[k, max_row], :k] = L[[max_row, k], :k]

        for i in range(k+1,n):
            if abs(U[k,k]) < 1e-12:
                factor = 0.0
            else:
                factor = U[i, k] / U[k, k]
            L[i,k] = factor
            U[i, k:] = U[i, k:] - factor * U[k, k:]

    return P, L, U

# Task b)
# Implement a method, calculating the determinant of A.
# Input: Matrix A - 2D numpy array (e.g. np.array([[1,2],[3,4]]))
# Output: The determinant - a floating number
def determinant(A):
    n, m = A.shape

    if n == m == 0:
        return 0
    if n == m == 1:
        return A[0, 0]
    if n == m == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

    P,L,U = lu(A)
    #determinant L = 1 / det(L)*det(U) = det(A)
    detU = 1
    for k in range(n):
        detU = detU * U[k,k]
    return detU
