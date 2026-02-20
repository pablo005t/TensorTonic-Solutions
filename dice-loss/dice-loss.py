import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    p = np.array(p).flatten()
    y = np.array(y).flatten()
    Dice = 2 * np.sum(p*y) + eps
    Dice = Dice / (np.sum(p+y)+eps)
    return 1-Dice