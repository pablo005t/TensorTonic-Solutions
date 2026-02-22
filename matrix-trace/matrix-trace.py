import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    tr = 0
    for i in range(len(A)):
        tr = tr + A[i][i]
    return tr