def image_histogram(image):
    import numpy as np
    """
    Compute the intensity histogram of a grayscale image.
    """
    hist = np.zeros(256)
    for line in image:
        for i in line:
            hist[i] = hist[i] + 1
    return list(hist)
    # Write code here