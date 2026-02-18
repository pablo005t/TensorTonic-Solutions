import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    e = np.exp(-np.array(x))
    sigma = 1 / (1+e)
    return sigma
    # Write code here
