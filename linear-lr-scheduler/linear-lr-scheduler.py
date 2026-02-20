def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    Lr = 0
    if total_steps == 0:
        return final_lr
    elif step < warmup_steps:
        Lr = step * initial_lr / warmup_steps
    elif warmup_steps<= step <= total_steps:
        num = total_steps-step
        den = total_steps-warmup_steps
        Lr = final_lr + (initial_lr - final_lr) * num/den
    else:
        Lr = final_lr
    return Lr
