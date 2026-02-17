import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    if axis == 0:
        n_features = len(X[0])
        n_data = len(X)
        scale = [[] for l in X]
        for n in range(n_features):
            max_f = X[0][n]
            min_f = X[0][n]
            for c in range(n_data):
                if max_f < X[c][n]:
                    max_f = X[c][n]
                if min_f > X[c][n]:
                    min_f = X[c][n]
            if max_f == min_f:
                den = eps
            else:
                den = max_f - min_f
            for i in range(len(scale)):
                normal = X[i][n] - min_f
                normal = normal / den
                scale[i].append(normal)
        return scale
    else:
        scale = [] 
        for x in X:
            maximo = max(x)
            minimo = min(x)
            den = max ([maximo - minimo,eps])
            scale.append([(l-minimo)/den for l in x])
        return scale
            

