def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    def max(list):
        max = list[0]
        for i in list:
            if i> max:
                max = i
        return max
    lag_ = []
    for i in [ j for j in range(len(series)) if j>(max(lags) - 1)]:
        l = []
        for lag in lags:
            k = i-lag
            l.append(series[k])
        lag_.append(l)
    return lag_
            
            # Write code here