import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    if axis == 0:
        average = np.mean(X, axis = axis)
        std_ = np.std(X , axis = axis)
        std_ = np.maximum(std_, std_ + eps)
        return (X - average) / std_
    else:
        Z =[]
        for x in X:
            average = np.mean(x)
            std_ = np.std(x)
            std_ = np.maximum(std_, eps)
            z = (x - average) / std_
            Z.append(z)
        return Z