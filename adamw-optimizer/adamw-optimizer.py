import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    g = grad
    m = beta1 * np.array(m) + (1-beta1)*np.array(g)
    v = beta2 * np.array(v) + (1-beta2)*np.square(np.array(g))
    w = (1 - lr*weight_decay) * np.array(w) - lr*m/(np.sqrt(v)+eps)
    return (w, m, v)