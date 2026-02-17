def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    import numpy as np

    x = np.array(values, dtype=float)
    x_sorted = np.sort(x)
    n = len(x_sorted)
    if len(set(values)) == 1:
        return [0 for l in values]
    median = np.median(x_sorted)
    if n % 2 == 1:
        lower = x_sorted[:n//2]
        upper = x_sorted[n//2+1:]
    else:
        lower = x_sorted[:n//2]
        upper = x_sorted[n//2:]

    Q1 = np.median(lower)
    Q3 = np.median(upper)
    IQR = Q3 - Q1

    if Q1!= Q3:
        return ((x - median) / IQR).tolist()
