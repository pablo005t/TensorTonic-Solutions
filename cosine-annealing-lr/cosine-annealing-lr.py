import numpy as np
def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    lr = min_lr
    dif = base_lr - min_lr
    factor = 1+np.cos(np.pi*current_step/total_steps)
    lr = lr + dif * factor / 2
    return lr