import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if np.sum(np.array(p)) != 1:
        raise ValueError("No es una probabilidad")
    E = 0
    for i in range(len(x)):
        E += x[i]*p[i]
    return E 
    # Write code here
 