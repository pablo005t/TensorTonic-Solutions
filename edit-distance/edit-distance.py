import numpy as np
def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Usamos listas de Python para evitar errores de tipos de NumPy
    # y mejorar la compatibilidad en plataformas de ejercicios.
    M = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Inicialización de las filas y columnas base
    for i in range(m + 1):
        M[i][0] = i
    for j in range(n + 1):
        M[0][j] = j
        
    # Llenado de la matriz
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s1[i-1] != s2[j-1]:
                # Costo de: Inserción, Eliminación, Sustitución
                M[i][j] = 1 + min(M[i-1][j], M[i][j-1], M[i-1][j-1]) 
            else:
                M[i][j] = M[i-1][j-1]
                
    return int(M[m][n])