################################################################################
import sys
import numpy as np
import math as m
import numpy.linalg as nl
import scipy.linalg as sl
import xml.etree.ElementTree as et 
################################################################################

def XML_Extraction(XMLFILE): 
	tree = et.parse(XMLFILE)
	root = tree.getroot()
	n = int(root[0].text)
	f = lambda X : np.array(eval(root[1].text))
	D = "["
	for i in range(n):
		D += root[2][i].text
		if(i<n-1):
			D += ","
	D += "]"
	Df = lambda X : np.array(eval(D))

	A = ["0"]*n
	for i in range(0,n):
		A[i] = ["0"]*n
	d = [""]*n
	for i in range(n):
		d[i] = root[3][i].text
	u_ele = int((n*(n-1)) / (2))
	u = [""]*u_ele
	for i in range(u_ele):
		u[i] = root[3][n+i].text
	u_counter = 0
	for i in range(n):
		for j in range(i,n):
			if(i==j):
				A[i][i] = d[i]
			else:
				A[i][j] = u[u_counter]
				A[j][i] = u[u_counter]
				u_counter +=1
	H = "[["
	for i in range(n):
		for j in range(n):
			H += A[i][j]
			if(j<n-1):
				H += (",")
			else:
				if(i<n-1):
					H += "],["
	
	H += "]]"
	Hf = lambda X : np.array(eval(H))
	return (n,f,Df,Hf)

def Newton_Iteration(Df,Hf,X_curr):
	X_next = np.subtract(X_curr, nl.solve(Hf(X_curr), Df(X_curr)))
	return X_next

def Classify_Point(f,Hf,X):
	S = sl.eigvalsh(Hf(X))
	np.set_printoptions(precision=2)
	print("X is: ", X, "F(X) is: ", f(X))
	has_pos = False
	has_neg = False
	if(all(i > 0 for i in S)):
		return "Eignevalues are :", S, "it's a minimum point"
	if(all(i < 0 for i in S)):
		return "Eignevalues are :", S, "it's a maximum point"
	for i in S:
		if(i>0):
			has_pos = True
		if(i<0):
			has_neg = True
	if(has_pos == True and has_neg == True):
		return "Eignevalues are :", S, "it's a saddle point"	
	return "Eignevalues are :", S, "unclassifiable"

def Extremal_Points(XMLFILE,X_curr):
	tol = 10e-14
	n, f, Df, Hf = XML_Extraction(XMLFILE)
	X_next = Newton_Iteration(Df,Hf,X_curr)
	while(abs(nl.norm(X_next,np.inf)-nl.norm(X_curr,np.inf))>tol):
		X_curr = X_next
		X_next = Newton_Iteration(Df,Hf, X_curr)
	print(Classify_Point(f, Hf, X_next))

#c)
print("c)")
Extremal_Points("1c.xml", np.array([-2,0]))
Extremal_Points("1c.xml", np.array([-1,-1]))
Extremal_Points("1c.xml", np.array([0,0]))

#d)
print("d)")
Extremal_Points("1d.xml", np.array([-m.sqrt(2),0]))
Extremal_Points("1d.xml", np.array([0,0]))
Extremal_Points("1d.xml", np.array([0,-m.sqrt(2)]))
Extremal_Points("1d.xml", np.array([0,m.sqrt(2)]))
Extremal_Points("1d.xml", np.array([m.sqrt(2),0]))

#e)
print("e)")
Extremal_Points("1e.xml", np.array([-1,0]))
Extremal_Points("1e.xml", np.array([0,0]))
Extremal_Points("1e.xml", np.array([0,-1]))
Extremal_Points("1e.xml", np.array([0,1]))
Extremal_Points("1e.xml", np.array([1,0]))

#f)
print("f)")
Extremal_Points("1f.xml", np.array([-2,-2,2]))
Extremal_Points("1f.xml", np.array([-2,2,-2]))
Extremal_Points("1f.xml", np.array([0,0,0]))
Extremal_Points("1f.xml", np.array([2,-2,-2]))
Extremal_Points("1f.xml", np.array([2,2,2]))
