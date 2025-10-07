import numpy as np

# Task a)
# Implement the gaussian elimination method, to solve the given system of linear equations;
# Add partial pivoting to increase accuracy and stability of the solution;
# Return the solution for x
# Assume a square matrix
def solveLinearSystem(A, b):
    A = A.astype(float)            # Sicherheitshalber in float konvertieren
    b = b.astype(float).copy()
    n = len(b)
    x = np.zeros(n)

    #Elimination
    for k in range(n-1):
        max_row = np.argmax(np.abs(A[k:, k])) + k
        if A[max_row, k] == 0:
            continue
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        for i in range(k+1,n):
            factor = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]


    if isConsistent(A, b):
    # Rückwärtseinsetzen
        for i in range(n-1, -1, -1):
            if A[i, i] == 0:
                x[i] = b[i]         #theoretically infinetly many solutions, but assume x[i] = b[i], to get one solution
            else:
                x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]

        return x

    return False




# Task b)
# Implement a method, checking whether the system is consistent or not;
# Obviously, you're not allowed to use any method solving that problem for you.
# Return either true or false
def isConsistent(A, b):
    A = A.astype(float)
    b = b.astype(float).copy()
    n, m = A.shape

    for k in range(min(n, m)):
        max_row = np.argmax(np.abs(A[k:, k])) + k
        if A[max_row, k] == 0:
            continue
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    for i in range(n):
        if np.allclose(A[i], 0) and not np.isclose(b[i], 0):
            return False

    return True


# Task c)
# Implement a method to compute the daily amounts of chicken breast, brown rice, black beans and avocado to eat to achieve the daily nutritional intake described in the exercise;
# Return a vector x with the grams of chicken breast, brown rice, black beans and avocado to eat each day.
def solveNutrients(A, b):
    sol = solveLinearSystem(A, b)
    sol = sol * 10
    sol_rounded = np.ceil(sol)
    return sol_rounded
