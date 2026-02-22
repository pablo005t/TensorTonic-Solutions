import numpy as np
def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    # Write code here
    m = len(s1)
    n = len(s2)
    M = np.zeros((m + 1, n + 1), dtype = int)
    for i in range(m+1):
        M[i][0] = i
    for i in range(n+1):
        M[0][i] = i
    for j in range(1,n+1):
        for i in range(1,m+1):
            if s1[i-1] != s2[j-1]:
                M[i][j] = 1 + min(M[i-1][j], M[i][j-1], M[i-1][j-1]) 
            else:
                M[i][j] = M[i-1][j-1]
    return int(M[m][n])