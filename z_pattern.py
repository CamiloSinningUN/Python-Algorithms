import numpy as np
# Funcion recursiva BigZ.
def Big_Z(i, j, k):
  Z[i][j] = k
  Z[(n-1)-i][(n-1)-j] = n**2-(k-1)
  #print(Z,'\n')
  if i == (n-1)//2 and j == n//2:  #CASO BASE
    return Z
  elif i <= (n-2)//3 and j == i:  #SINGULARIDAD 3.1
    Big_Z(i, j+1, k + 1)
  elif i <= (n-2)//3 and j == n-1-2*i:  #SINGULARIDAD 3.2
    Big_Z(i + 1, j - 1, k + 1)
  elif j<=(n-3)//3 and i == n-2-2*j:  #SINGULARIDAD 3.3
    Big_Z(i-1, j, k + 1)
  else:   #LLAMADOS RECURSIVOS MÁS PEQUEÑOS
    if j > i and j <  n-1-2*i: #4.1 HACIA LA DERECHA
      Big_Z(i, j+1, k + 1)
    elif i > j and i < n-2-2*j: #4.2 4.3 HACIA ARRIBA
      Big_Z(i - 1, j, k + 1)
    else: # DIAGONAL SECUNDARIA DESDE N-E HACIA S-O
      Big_Z(i+1, j-1, k + 1)

def rotarZ(i,j):
  temp=Z[i][j]
  Z[i][j]=Z[n-1-j][i]
  Z[n-1-j][i]=Z[n-1-i][n-1-j]
  Z[n-1-i][n-1-j]=Z[j][n-1-i]
  Z[j][n-1-i]=temp

  if(i == n//2 and j == n//2):
    return Z
  elif(j == n-2-i):
    rotarZ(i+1,i+1)
  else:
    rotarZ(i,j+1)



# Programa principal
n = int(input('Digite número entero: '))
Z = np.zeros((n, n))
Big_Z(n//3, (n-1)//3, 1)

print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in Z
]))
print("\n\n")
rotarZ(0,0)

# Imprimir rombo
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in Z
]))