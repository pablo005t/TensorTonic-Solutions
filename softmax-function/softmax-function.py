import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
"""
    x = np.array(x)
    if x.ndim == 2:
        m = np.max(x, axis = 1, keepdims=True)
        x = x-m
        softmax = np.exp(x) / np.sum(np.exp(x), axis = 1, keepdims = True)
    else:
        m = np.max(x)
        x = x-m
        softmax = np.exp(x) / np.sum(np.exp(x))
    return softmax

    