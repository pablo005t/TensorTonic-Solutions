def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    W = len(X)//pool_size
    H = len(X[0])//pool_size
    out = []
    for i in range (W):
        line = []
        for j in range(H):
            mean = 0
            for n in range(pool_size):
                for k in range(pool_size):
                    pixel = X[i*pool_size + n][j*pool_size + k]
                    mean += pixel
            mean = mean / pool_size**2
            line.append(mean)
        out.append(line)
    return out
    # Write code here