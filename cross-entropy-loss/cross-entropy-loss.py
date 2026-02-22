import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    cross = 0
    for i,y in enumerate(y_true):
        cross = cross - np.log(y_pred[i][y])
    return cross/len(y_true)