import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.asarray(g)
    norm = np.linalg.norm(g)
    if norm == 0 or max_norm <=0:
        return g
    elif norm <=max_norm:
        return(g)
    else:
        return( g*max_norm/norm)
