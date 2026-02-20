import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    G = np.array(G) + np.square(np.array(g))
    w = w - lr * np.array(g) / np.sqrt(G + eps)
    return (w,G)