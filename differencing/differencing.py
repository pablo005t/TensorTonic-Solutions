def difference(list):
    dif = []
    for i in range(1, len(list)):
        d = list[i] - list[i-1] 
        dif.append(d)
    return dif

def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    d = [x for x in series]
    for i in range(order):
        d = difference(d)
    return d