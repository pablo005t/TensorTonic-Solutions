import numpy as np

def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    m = beta1 * np.array(m) + (1-beta1) * np.array(grad)
    v = beta2 * np.array(v) + (1-beta2) * np.square(np.array(grad))
    w = w - lr * (beta1* m + (1-beta1) * np.array(grad))/(np.sqrt(v) + eps)

    return (w,m,v)