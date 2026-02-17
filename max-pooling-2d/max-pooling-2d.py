import numpy as np
def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    W = len(X)//pool_size
    H = len(X[0])//pool_size
    out = []
    for i in range (W):
        line = []
        for j in range(H):
            max = X[i*pool_size][j*pool_size]
            for n in range(pool_size):
                for k in range(pool_size):
                    pixel = X[i*pool_size + n][j*pool_size + k]
                    if max < pixel:
                        max = pixel
            line.append(max)
        out.append(line)
    return out
    # Write code here