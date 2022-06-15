import numpy as np


def cuadro_raro(i, j, k):
    C[i][j] = k
    if i == n - 2 and j == n - 1 and k == ne:
        return C
    elif i == n - 1 and j == n - 1:
        cuadro_raro(0, 1, k + 1)
    elif (j == 0 or i == n-1) and (j - i) % 2 == 0 and j - i <= 0:
        cuadro_raro(((i + j + 1) + 1) // 2, ((i + j + 1) - 1) // 2, k + 1)
    elif (j == 0 or i == n-1) and (j - i) % 2 == 1 and j - i <= 0:
        cuadro_raro(((i + j + 1)) // 2, ((i + j + 1)) // 2, k + 1)
    elif (j == n-1 or i == 0) and (j - i) % 2 == 1 and j - i > 0:
        cuadro_raro(((i + j + 1) - 2) // 2, ((i + j + 1) + 2) // 2, k + 1)
    elif (j == n-1 or i == 0) and (j - i) % 2 == 0 and j - i > 0:
        cuadro_raro(((i + j + 1) - 1) // 2, ((i + j + 1) + 1) // 2, k + 1)
    else:
        if j - i > 0:
            cuadro_raro(i - 1, j + 1, k + 1)
        else:
            cuadro_raro(i + 1, j - 1, k + 1)



n = int(input("digite un numero:"))
ne = n**2

C = np.zeros((n, n))
cuadro_raro(0, 0, 1)
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in C
]))
