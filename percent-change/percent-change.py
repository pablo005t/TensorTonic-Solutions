def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    pct =[]
    for i in range(1,len(series)):
        p = series[i]-series[i-1]
        if series[i-1] == 0:
            p = 0
        else:
            p = p/series[i-1]
        pct.append(p)
    return pct
    # Write code here