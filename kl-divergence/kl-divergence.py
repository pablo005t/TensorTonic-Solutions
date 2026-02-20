import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    p = np.array(p)
    q = np.array(q)
    D = np.sum(p*np.log(p/q))
    # Write code here
    return D
    