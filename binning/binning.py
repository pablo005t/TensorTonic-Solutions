def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    import numpy as np
    def maxi(list):
        max = list[0]
        for i in list:
            if i> max:
                max = i
        return max
    values_ = [-l for l in values]
    max = maxi(values)
    min = - maxi(values_) 
    width = max - min
    width = width / num_bins
    bin = []
    if width == 0: 
        return [0 for l in values]
    for i in values:
        f = i - min
        f = f / width 
        x = - np.floor(f)
        
        y = - num_bins + 1
        bin_i = - maxi( [x, y])
        bin.append(bin_i)
    return bin
    # Write code here