def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    import numpy as np
    # Write code here
    encoding =[]
    for val in values:
        theta = 2*np.pi*val / period
        cos = np.cos(theta)
        sin = np.sin(theta)
        encoding.append([sin, cos])
    return encoding