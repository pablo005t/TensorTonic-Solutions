import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    pad_seq = []
    if max_len == None:
        max_len = np.max(np.array([len(l) for l in seqs]))
    for seq in seqs:
        pad_s = [a for a in seq]
        while len(pad_s) < max_len:
            pad_s.append(pad_value)
        if len(pad_s)> max_len:
            pad_s = pad_s[0:max_len]
        pad_seq.append(pad_s)
    return np.array(pad_seq)