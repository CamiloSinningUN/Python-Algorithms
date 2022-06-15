import numpy as np

def triangulo(i,j,k):
  T[i][j] = k
  jv = j-abs(i-iv)
  if k == nc**2:
    return T
  elif i == 2*j and i>iv:
    triangulo(nf-i,j-1,k+1)
  elif i-iv==j-jv and i==2*j+1 and i>iv:
    triangulo(nf-i,j,k+1)
  else:
    if i >= nf-1-2*j and i<= 2*j:
      triangulo(i+1,j,k+1)
    else:
      triangulo(i+1,abs(iv-(i+1))+jv,k+1)
  

while True:
  nc = int(input("Digita un numero entero par n:"))
  if nc % 2 ==0:
    break

nf = 2*nc-1
iv = nf//2
T = np.zeros((nf,nc))
triangulo(0,nc-1,1)

# Imprimir rombo
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in T
]))