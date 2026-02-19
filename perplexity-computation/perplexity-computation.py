import numpy as np
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    H = 0
    for i in range(len(actual_tokens)):
        token = actual_tokens[i]
        prob = prob_distributions[i][token]
        H = H + np.log(prob)
    H = - H/len(actual_tokens)
    PP = np.exp(H)
    return PP