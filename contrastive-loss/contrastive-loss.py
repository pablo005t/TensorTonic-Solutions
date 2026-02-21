import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    a = np.array(a)
    b = np.array(b)
    y = np.array(y)
    if b.ndim != 1:
        d = np.linalg.norm(a-b, axis = 1)
    else:
        d = np.linalg.norm(a-b)
    l = y* np.square(d) + (1-y) * np.square(np.where(d < margin, margin-d, 0 ))
    
    if reduction == "mean":
        return np.mean(l)
    else:
        return np.sum(l)