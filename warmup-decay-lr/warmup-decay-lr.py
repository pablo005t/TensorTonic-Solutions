def warmup_decay_schedule(base_lr, warmup_steps, total_steps, current_step):
    """
    Compute the learning rate at a given step using warmup + linear decay.
    """
    lr = base_lr
    if warmup_steps>current_step:
        lr = lr * current_step / warmup_steps
    else:
        lr = lr * (total_steps - current_step) /(total_steps - warmup_steps)

    return lr