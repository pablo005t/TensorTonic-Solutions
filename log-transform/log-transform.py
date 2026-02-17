def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    import numpy as np
    return [np.log(1+x) for x in values]