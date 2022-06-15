import numpy as np

# Funcion recursiva rombo por capas.
def rombo(i, j, k):
  R[i][j] = k
  if i == n//2 and j == n//2 : #Caso base
    return R
  elif i<=v and j == v+1: #Singularidad
    rombo(i,j-1,k+1) 
  else: #LLamados recursivos mas pequeños9
    if j<v or (i<v and j==v):  
      jv=j-abs(iv-i)
      rombo(i+1,abs(iv-(i+1))+jv,k+1)
    else:
      jv=j+abs(iv-i)
      rombo(i-1,-abs(iv-(i-1))+jv,k+1)
      

#Lectura de tamaño de matriz
while True:
  n = int(input("Digita un numero entero n:"))
  if n % 2 ==1:
    break

v = int(((n-1)/2))
iv = v
ne = (v+1)**2+(v)**2
R = np.zeros((n,n))
rombo(0,v,1)

# Imprimir rombo
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in R
]))