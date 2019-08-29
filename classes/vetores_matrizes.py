import numpy as np
from numpy.linalg import det,inv,eig

'''def soma(a, b):
    soma = a + b
    return  soma
print(soma(5,6))

'''
#matriz diagonal
print(np.diag([1,5,7,9,10,1]))
#matriz nula
print(np.zeros([2,20]))
#matriz identidade
#o  numero dentro dos parenteses representam a dimensao
print(np.identity(4))

A = np.array([[1,0,3],[2,1,4]])
print('A =', A)
#matriz transposta
#At = np.T
At = np.transpose(A)
print('At=',At)

a = 2
v1 = np.array([1,2,3,4,5])
r1 = v1 +  2
print(r1)

#operacoes entre vetores e matrizes, precisam ter as mesmas dimensoes
B = np.array(([1,1,1],[2,2,2]))
A = np.array([1,2,3])
G = B - A
print('G', G)


#operaces entre matrizes
D = np.array(([1,1], [2,2]))
E = np.array(([20,20], [40,40]))
F = np.array(([1,2,3], [4,5,6]))
S = D + E
print(S)
#multiplicacao entre matrizes
# a multiplicacao e realizada entre os elementos
print(np.multiply(D, E))

#traco de uma matriz

H = np.array(([1,1], [2,2]))
I = np.array(([1,1,1], [3,3,3]))
tr_A = np.trace(H)
print(tr_A)