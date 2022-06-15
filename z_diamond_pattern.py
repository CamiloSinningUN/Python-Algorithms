import numpy as np

def ramas(i,j,k):
  R[i][j] = k
  if(i == n//2 and j == n//2):
    return R
  elif (i>=v and j == v):
    ramas(n-i,v,k+1)
  else:
    if (k % 2 == 1):
      jv=(n-1-j)-abs(iv-i)
      ramas(i+1,abs(iv-(i+1))+jv,k+1)
    else:
      jv=(n-1-j)+abs(iv-i)
      ramas(i,-abs(iv-(i))+jv,k+1)
    

    

while True:
  n = int(input("Digita un numero entero n:"))
  if n % 2 ==1:
    break

v = int(((n-1)/2))
iv = v
ne = (v+1)**2+(v)**2
R = np.zeros((n,n))
ramas(0,v,1)

# Imprimir rombo
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in R
]))