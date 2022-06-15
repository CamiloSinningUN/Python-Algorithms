import numpy as np


def home_raro(i, j, k):
    H[i][j] = k
    if i == v and j == v and k == ne:
        return H
    elif i == v and j < v and j % 2 == 0:
        home_raro(n - 1 - j, 0, k + 1)
    elif j == 0 and i > v and i % 2 == 1:
        home_raro(v, i - 1, k + 1)
    elif i == v and j > v and j % 2 == 1 :
        home_raro(j, n - 1, k + 1)
    elif j == n - 1 and i > v and i % 2 == 0:
        home_raro(v, n - i, k + 1)
    else:
        iv = i - abs(j - jv)
        if i <= v and iv % 2 == 0:
            home_raro(iv + abs((j - 1) - jv), j - 1, k + 1)
        elif i <= v and iv % 2 == 1:
            home_raro(iv + abs((j + 1) - jv), j + 1, k + 1)
        elif i > v and i % 2 == 0:
            home_raro(i, j + 1, k + 1)
        else:
            home_raro(i, j - 1, k + 1)


while True:
    n = int(input("digite un numero impar:"))
    if n % 2 == 1:
        break

v = n // 2
jv = v
ne = (v + 1)**2 + n * (n - (v + 1))

H = np.zeros((n, n))
home_raro(v, n - 1, 1)
print('\n'.join([
    ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
    for row in H
]))
