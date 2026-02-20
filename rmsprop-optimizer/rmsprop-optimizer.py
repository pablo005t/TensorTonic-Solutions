import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    g = np.array(g)
    s = np.array(s)
    s = beta * s + (1 - beta) * np.square(g)
    w = np.array(w) - lr * g / np.sqrt(s+eps)
    return (w, s)