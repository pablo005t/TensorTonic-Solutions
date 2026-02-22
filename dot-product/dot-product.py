import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    if len(x)!=len(y):
        raise ValueError
    else:
        dot = 0
        x = np.array(x)
        y = np.array(y)
        d = x*y
        return np.sum(d)