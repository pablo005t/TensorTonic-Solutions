import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    if len(vocab) == 0:
        return np.array([], dtype=int)
    elif len(tokens) == 0:
        return np.array([0]*len(vocab), dtype=int)
    bag = []
    for v in vocab:
        cont = 0
        for token in tokens:
            if token == v:
                cont = cont + 1
        bag.append(cont)
    return np.array(bag)