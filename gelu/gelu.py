import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x = np.array(x)
    erf_vectorizada = np.vectorize(lambda x: 1 + math.erf(x / math.sqrt(2)))
    erf = erf_vectorizada(x)
    G = x * erf /2
    return G

