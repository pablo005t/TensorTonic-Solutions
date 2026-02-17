def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    def cum(hist, i):
        cum = 0
        for j in range(i+1):
            cum = cum + hist[j]
        return cum
    import numpy as np 
    hist = np.zeros(256)
    total = 0
    for line in image:
        for pixel in line:
            hist[pixel] += 1
            total += 1
    for i in range(256):
        if hist[i] != 0:
            min = hist[i]
            break
    hist_eq = []
    for line in image:
        line_eq = []
        for pixel in line:
            if total - min != 0 :
                pix_eq = round((cum(hist,pixel) - min) / (total - min) * 255)
            else:
                pix_eq = 0
            line_eq.append(pix_eq)
        hist_eq.append(line_eq)
    return  hist_eq
    # Write code here