import numpy as np

# Funcion recursiva Home.
def Home(i, j, k):
  H[i][j] = k
  if k == ne:  #CASO BASE
    return H
  elif i < v and j == v+i:  #SINGULARIDAD 1
    Home(i+1, v-(i+1), k + 1)
  elif i >= v and j == nc-1:  #SINGULARIDAD 2
    Home(i+1, 0, k + 1)
  else:   #LLAMADOS RECURSIVOS MÁS PEQUEÑOS
    Home(i,j+1,k+1)

      
# Programa principal
w=True
while w:
  nc = int(input('Digite número entero impar de columnas :'))
  if nc % 2 == 1:
    w=False 
  else:
    print("dijite un numero impar, por favor")
    
v =int((nc-1)/2) 

w=True
while w:
  nf = int(input('Digite número entero de filas superior a '+str(v+1)+":"))
  if nf >v:
    w=False 
  else:
    print("dijite un numero superior a "+v+", por favor" )
    
ne=v*v+nc*(nf-v)
H = np.zeros((nf, nc))
Home(0,v,1)

# Imprimir Home
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in H
]))
  
