def acceso_medio(N_b, R, S, V):
  T_E = N_b/(R)
  R_E = S/V

  print("Tiempos de vulnerabilidad: ")
  print("aloha puro: "+str((T_E*2))+"seg")
  print("aloha ranurado: "+str(T_E)+"seg")
  print("csma: "+str(R_E))
  print("\n")

  P_U = N_b-18*8
  print("parte util en trama csma persistente ethernet clasica: \n + "+str(P_U)+" bits \n + "+str(P_U/8)+" bytes")

def codificacion(B):
  b_n = list(B)
  print("codificación binaria: ")
  cod_b = ""
  for i in b_n:
    if i == "1":
      cod_b = cod_b +"-"
    elif i == "0":
      cod_b = cod_b +"_"
    else:
      print("no es un número binario")
      break
  print(cod_b)

  print("codificación machester: ")
  cod_b = ""
  for i in b_n:
    if i == "1":
      cod_b = cod_b +"_|-"
    elif i == "0":
      cod_b = cod_b +"-|_"
    else:
      print("no es un número binario")
      break
  print(cod_b)


  print("codificación machester diferencial: ")
  cod_b = ""
  ar_b = "-|_"
  for i in b_n:
    if i == "0":
      if ar_b == "_|-":
        cod_b = cod_b +"_|-"  
        ar_b = "_|-"
      else:
        cod_b = cod_b +"-|_"  
        ar_b == "-|_"
    elif i == "1":
      if ar_b == "_|-":
        cod_b = cod_b +"-|_"  
        ar_b = "-|_"  
      else:
        cod_b = cod_b +"_|-"  
        ar_b = "_|-"

    else:
      print("no es un número binario")
      break
  print(cod_b) 
      
def IHL(B):
  n = int(B,2)
  print("La cabecera ocupa: "+str((n*32)/8)+" bytes")
  print("Tiene "+str(n)+" palabas de 32 bits")
  n1 = int(input("Digite:\n 1. si tiene la longitud total \n 2. sino la tiene"))
  if n1 == 1:
    l = float(input("digite la longitud total (bytes)"))
    print("El tamaño de los datos de este paquete es: "+str(l-((n*32)/8))+" bytes")

def W_clase(B):
  ar = B.split(".")
  bi = bin(int(ar[0])).replace("0b","")
  bi_a = list(bi)

  if len(bi_a)<8:
    while not len(bi_a) == 8:
      bi_a.insert(0,"0")
  if bi_a[0] == "0":
    print("Clase A")
    print(" id_red: "+str(ar[0])+".0.0.0 \n id_host: 0."+str(ar[1])+"."+str(ar[2])+"."+str(ar[3]))

  elif bi_a[0] == "1" and bi_a[1] == "0":
    print("Clase B")
    print(" id_red: "+str(ar[0])+"."+str(ar[1])+".0.0 \n id_host: 0.0."+str(ar[2])+"."+str(ar[3]))

  elif bi_a[0]=="1" and bi_a[1] == "1" and bi_a[2]=="0":
    print("Clase C")
    print(" id_red: "+str(ar[0])+"."+str(ar[1])+"."+str(ar[2])+".0 \n id_host: 0.0.0."+str(ar[3]))

  else:
    print("Non è niente")

#true es simplificada y false es extendida
# hallar red,subred y host
def mask(B,simp,m):
  #Crear mascara
  msk_t = ""
  if simp:
    for i in range(32):
      if (i)%8 == 0 and not i == 0:
        msk_t=msk_t+"."
      if(i<m):
        msk_t = msk_t+"1"
      else:
        msk_t = msk_t+"0"
    msk_s_t = msk_t.split(".")
    msk_s =[]
    for i in msk_s_t:
      msk_s.append(str(int(i,2)))
  else:
    msk = m
    msk_s = msk.split(".")

  ip_s = B.split(".")
  ip_red = []
  ip_subred = []
  ip_host = []
  for i in range(4):
    if(msk_s[i]=="255"):
      ip_red.append(int(ip_s[i]) & int(msk_s[i]))
      ip_subred.append(0)
      ip_host.append(0)
    elif msk_s[i]=="0":
      ip_host.append(int(ip_s[i]))
      ip_red.append(0)
      ip_subred.append(0)
    else:
      ip_subred.append(int(ip_s[i]) & int(msk_s[i]))
      ip_red.append(0)
      print(int(ip_s[i]))
      ip_host.append((int(ip_s[i])-(int(ip_s[i]) & int(msk_s[i]))))
  #imprimir
  print("ip de red es: ")
  print(ip_red)
  print("ip de subred es: ")
  print(ip_subred)
  print("ip de host es: ")
  print(ip_host)
    
#hallar mascara para subred y las direcciones 
def mask_seg(B,simp,m,segs):
  #Crear mascara
  msk_t = ""
  if simp:
    for i in range(32):
      if (i)%8 == 0 and not i == 0:
        msk_t=msk_t+"."
      if(i<m):
        msk_t = msk_t+"1"
      else:
        msk_t = msk_t+"0"
    msk_s_t = msk_t.split(".")
    msk_s =[]
    for i in msk_s_t:
      msk_s.append(str(int(i,2)))
  else:
    msk = m
    msk_s = msk.split(".")

  ip_s = B.split(".")
  bi = bin(int(segs)).replace("0b","")
  n_bi = list(bi)
  k = len(n_bi)
  num = ""
  for i in range(8):
    if i <k:
      num = num+"1"
    else:
      num = num+"0"

  sw = True

  for i in range(len(msk_s)):
    if not msk_s[i] == "255" and sw:
      msk_s[i] = int(num,2)
      sw = False
      num_t = i
  
  print("la mascara de subred es: ")
  print("Extendida:")
  print(msk_s)

  simp = 0
  mas_t = ""
  for i in msk_s:
    mas_t += str(bin(int(i)).replace("0b",""))
  
  for i in mas_t:
    if i == "1":
      simp+=1

  print("Simplificada:")
  print(simp)
  print("\n")
  print("las ip serian: ")
  l_num = list(num)
  for i in range(len(l_num)-1):
    if not (l_num[i+1]=="0"):
      l_num[i]="0"
  delta_t = ""
  for i in l_num:
    delta_t= delta_t+i
  delta = int(delta_t,2)
  for i in range(len(ip_s)):
    if (i>=num_t):
      ip_s[i] = "0"
  for i in range(segs):
    ip_s[num_t] = str(int(ip_s[num_t]) + delta)
    print(ip_s)

def wheel(simp,m):
  #Crear mascara
  msk_t = ""

  if simp:
    for i in range(32):
      if (i)%8 == 0 and not i == 0:
        msk_t=msk_t+"."
      if(i<m):
        msk_t = msk_t+"1"
      else:
        msk_t = msk_t+"0"
    msk_s = msk_t.split(".")
  else:
    msk = m
    print("Esto no sirve, da mal")
    msk_s_t = msk.split(".")
    msk_s = []
    msk_s = ["" for i in range(len(msk_s_t))] 
    for i in range(len(msk_s_t)):
      msk_s[i] = str(bin(int(msk_s_t[i])).replace("0b",""))

  msk_inv = []
  msk_inv = ["" for i in range(len(msk_s))] 

  for i in range(len(msk_s)):
    for j in msk_s[i]:
      if j == "1":
        msk_inv[i] += "0"
      else:
        msk_inv[i] +="1"
  
  ext = []
  for i in msk_inv:
    ext.append(str(int(i,2)))

  print("el wheelcart es:")
  print(ext)



print("WARNING: CUIDADO CON LAS UNIDADES")
n = int(input("Opciones: \n 1. capa de enlace \n 2. capa de red\n 3.bit host para vlsm"))
if n == 1:
  n1 = int(input("Opciones 2: \n 1. acceso al medio \n 2. codificación\n"))
  if n1 == 1:
    print("Dígite los siguientes datos sino tiene la info ")
    N_b = float(eval(input("tamaño paquete (bits)")))
    R = float(eval(input("Ancho de banda del enlace (bps)")))
    S = float(eval(input("Largo del enlace fisico (metros)")))
    V = float(eval(input("rapidez de propagación del medio(m/s)")))
    acceso_medio(N_b,R,S,V)
  elif n1 == 2:
    B = input("Digitar el binario: \n")
    codificacion(B)
  else:
    print("Fin del programa")
elif n == 2:
  n1 = int(input("Opciones 2: \n 1. IHL \n 2. Direccionamiento con clase\n 3. direccionamiento con mascara\n 4. Segmentos\n 5. Wheelcart (idk)"))
  if n1 == 1:
    B = input("Digite el binario:\n")   
    IHL(B)
  elif n1 == 2:
    B = input("Digite la dirección ip:\n")  
    W_clase(B)
  elif n1 == 3:
    B = input("Digite la dirección ip:\n") 
    n2 = int(input("Opcion 3: \n 1. Mascara simplificada \n 2. Mascara extendida\n "))
    if n2 ==1:
      m = int(input("digite la mascara (simplificada)\n"))
      mask(B,True,m)
    elif n2==2:
      m = input("digite la mascara (extendida)\n")
      mask(B,False,m)
    else:
      print("Fin del programa")
  elif n1 == 4:
    B = input("Digite la dirección ip:\n") 
    n_s = int(input("Digite el numero de segmentos: "))
    n2 = int(input("Opcion 3: \n 1. Mascara simplificada \n 2. Mascara extendida\n "))
    if n2 ==1:
      m = int(input("digite la mascara (simplificada)\n"))
      mask_seg(B,True,m,n_s)
    elif n2==2:
      m = input("digite la mascara (extendida)\n")
      mask_seg(B,False,m,n_s)
    else:
      print("Fin del programa")
  elif n1 == 5:
    n2 = int(input("Opcion 3: \n 1. Mascara simplificada \n 2. Mascara extendida\n "))
    if n2 ==1:
      m = int(input("digite la mascara (simplificada)\n"))
      wheel(True,m)
    elif n2==2:
      m = input("digite la mascara (extendida)\n")
      wheel(False,m)
    else:
      print("Fin del programa")
    
  else:
    print("Fin del programa")
elif n == 3:
  bh = int(input("ingrese el bit host"))
  temp_msk = ""
  sum = 32-bh
  for i in range(32):
    if i<sum:
      temp_msk = temp_msk+"1"
    else:
      temp_msk = temp_msk+"0"
  msk_f = []
  for i in range(4):
    msk_f.append(int(temp_msk[i*8:i*8+8],2))     
  
  print("la mascara es:")
  print(msk_f)
else:
  print("Fin del programa")
