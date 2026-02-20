import numpy as np 
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    predictions = np.array(predictions)
    targets = np.array(targets)
    prob = np.where(targets == 1, predictions, 1- predictions)
    F = -alpha * (1-prob)**gamma * np.log(prob)
    return np.mean(F)