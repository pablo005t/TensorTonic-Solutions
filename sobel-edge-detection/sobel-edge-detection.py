import numpy as np
def mult_mat(A,B):
        m = len(A)
        n = len(A[0])
        n_B = len(B)
        p = len(B[0])
        C = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C


def sobel_edges(image):
    # padding lateral
    image = [[0] + row + [0] for row in image]
    # padding arriba/abajo
    pad = [0] * len(image[0])
    image = [pad] + image + [pad]

    Kx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    Ky = [[-1,-2,-1],[0,0,0],[1,2,1]]

    Sobel = []
    for i in range(1, len(image) - 1):
        row_out = []
        for j in range(1, len(image[0]) - 1):
            # ventana 3x3
            cuad = [image[i + di][j + dj] for di in (-1,0,1) for dj in (-1,0,1)]
            # rearmar como 3x3 (opcional, para claridad)
            cuad = [cuad[0:3], cuad[3:6], cuad[6:9]]

            Gx = sum(Kx[u][v] * cuad[u][v] for u in range(3) for v in range(3))
            Gy = sum(Ky[u][v] * cuad[u][v] for u in range(3) for v in range(3))

            row_out.append(float(np.sqrt(Gx*Gx + Gy*Gy)))
        Sobel.append(row_out)

    return Sobel