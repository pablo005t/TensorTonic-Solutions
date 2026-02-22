import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    actual = x_t @ Wx
    past = h_prev @ Wh
    inp = actual+past+b
    return np.tanh(inp)