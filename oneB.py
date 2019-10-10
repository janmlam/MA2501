import numpy as np

d = np.array([11,22,33,44,55,66])
u = np.array([12,13,14,15,16, 23,24,25,26, 34,35,36, 45,46, 56])
n=6
A = np.empty([n,n])
'''
for i in range(n): #O(n)
	A[i][i] = d[i]
'''

u_counter = 0
for i in range(n):
	for j in range(i,n):
		if(i==j):
			A[i][i] = d[i]
		else:
			A[i][j] = u[u_counter]
			A[j][i] = u[u_counter]
			u_counter +=1
print(A)

#kandidatnr: 10012
#studentnr: 478790