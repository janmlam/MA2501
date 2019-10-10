################################################################################
import sys
import os
import math as m 
import numpy as np
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
################################################################################


def XML_Extraction(XMLFILE):
	tree = et.parse(XMLFILE)
	root = tree.getroot()
	f0 = lambda x : np.array(eval(root[0][0].text))
	f1 = lambda x : np.array(eval(root[0][1].text))
	I = [int(root[1][0].text), int(root[1][1].text)]
	print(f0(0))
	print(I[0])
	#I_1 = int(root[1][1].text)

XML_Extraction("f2.xml")

def Collect_Data(): #PREFIX,METHOD,GRID,I
	data_list = []
	directory = "C:\\Users\Jan\Dropbox\ITGK\iiii"

	for file in os.listdir(directory):
		os.chdir(directory)
		filename = os.fsdecode(file)
		if filename.endswith(".txt"):
			f = open(filename, 'r')
			for line in f:
				line = line.strip("\n")
				data_list.append(line)
			f.close()
		else:
			continue
	#print(data_list)

    #return DATA,T,PATH

Collect_Data()
'''
def Interpolation_Program(XMLFILE,PROGRAM,METHOD,GRID,n):



def Partition(GRID,I,n):


def Compute_Points(PREFIX,METHOD,GRID,f0,f1,I,X,n):


def Lagrange_Newton_Coefficients(f0,X,n):
    return a


def Lagrange_Newton_Evaluation(X,a,n,t):
    return P


def Hermite_Newton_Coefficients(f0,f1,X,n):
    return a,Z


def Hermite_Newton_Evaluation(Z,a,n,t):
    return H




def Plot_Error(PATH,DATA,f0,T):


def Plot_Polynomials(PATH,DATA,f0,X):
'''