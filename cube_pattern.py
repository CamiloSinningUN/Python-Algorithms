import numpy as np

#Función recursiva para cubo con capas
def cubo_capas(i, j, k, num):

    C_caso1[k][i][j] = num #Caso 1
    C_caso2[j][i][k] = num #Caso 2
    C_caso3[i][k][j] = num #Caso 3
    if num == ne: #Caso base
        return C_caso1, C_caso2, C_caso3
    elif num == (ne/n)*(k+1): #Singularidad 1
        cubo_capas(0, 0, k + 1, num + 1)
    elif j - i == 1 and i < v: #Singularidad 2
        cubo_capas(i + 1, j, k, num + 1)
    else: #Llamados recursivos más pequeños
        if j - i <= 0 and j < v and i + j < n - 1:
            cubo_capas(i + 1, j, k, num + 1)
        elif j - i < 0 and i >= v and j + i >= n - 1:
            cubo_capas(i, j + 1, k, num + 1)
        elif j - i >= 0 and j >= v and j + i > n - 1:
            cubo_capas(i - 1, j, k, num + 1)
        else:
            cubo_capas(i, j - 1, k, num + 1)

#Lectura de tamaño de cubo
n = int(input("Digita un numero entero impar n:"))

v = n // 2
ne = n**3
C_caso1 = np.zeros((n, n, n))
C_caso2 = np.zeros((n, n, n))
C_caso3 = np.zeros((n, n, n))
cubo_capas(0, 0, 0, 1)

#Se imprimen los 3 casos
print("Caso 1:")
print(C_caso1)
print("\n\n")
print("Caso 2:")
print(C_caso2)
print("\n\n")
print("Caso 3:")
print(C_caso3)
