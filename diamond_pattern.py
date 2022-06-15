import numpy as np

def rombo(i,j,k):
  R[i][j] = k
  if i == n-2 and j == v and k == ne:
    return R
  elif i == n-1 and j == v:
    rombo(1,v,k+1)
  elif (j-i == -v and i%2==0)or (j-i == v and i%2==1):
    rombo(i+1,j+1,k+1)
  elif j+i==n+v-2:
    rombo((v-j+i+3)//2,(j-i+v-1)//2,k+1)
  else:
    if (j+i)%2 == 0 and ((i+j-v)/2)%2 == 0:
      rombo(i+1,j-1,k+1)
    elif (j+i)%2 == 0 and ((i+j-v)/2)%2 == 1:
      rombo(i-1,j+1,k+1)
    else:
      rombo(i+1,j+1,k+1)
  

while True:
  n = int(input("Digita un numero entero impar n:"))
  if n % 2 ==1:
    break

v = int(((n-1)/2))
ne = (v+1)**2+(v)**2
R = np.zeros((n,n))
rombo(0,v,1)

# Imprimir rombo
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in R
]))
