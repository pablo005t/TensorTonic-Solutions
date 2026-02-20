import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    Diff = y_pred - y_true
    MSE = np.sum(np.square(Diff))
    MSE = MSE /len(Diff)
    return MSE
