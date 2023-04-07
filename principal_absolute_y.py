import numpy as np
from numpy import polyfit
import matplotlib.pyplot as plt
import matplotlib as mpl

#mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['mathtext.default'] = 'it'
mpl.rcParams['font.size'] = 7
mpl.rcParams['legend.fontsize'] = 'large'		#relative size to font.size
mpl.rcParams['figure.titlesize'] = 'medium'     #relative size to font.size

##################################################################################################

#####################################
fa = open("stress_labcoord.txt","r")
fb = open("principal_stress.txt","w")

#for _ in range(1):
#	next(fa)
	
#T=np.array([[0,0,0],[0,0,0],[0,0,0]])
j=0
for line in fa:
	c0=line
	c = line.split(" ")
	c1 = np.array(c[:-1])
#	print(c1)
	n1 = c1.astype(np.float64)
	sx=n1[6]
	sy=n1[7]
	sz=n1[8]
	sxy=n1[9]
	sxz=n1[10]
	syz=n1[11]
	T=np.array([[sx,sxy,sxz],[sxy,sy,syz],[sxz,syz,sz]])
	values , vectors = np.linalg.eig(T)
	
	vc=np.transpose(vectors)
	total=np.append([values[:]],vc[:],axis=0)
	total=total[:,total[0,:].argsort()]
	vsorted=np.flip(total,axis=1)
	if vsorted[2,0]<0:
		vsorted[1:4,0:2]=-vsorted[1:4,0:2]
	s1=0.5*(vsorted[0,0]-vsorted[0,2])
	s2=0.5*(vsorted[0,0]-vsorted[0,1])
	s3=0.5*(vsorted[0,1]-vsorted[0,2])
	
	shearOCT=np.sqrt(4*(s1**2+s2**2+s3**2)/9)
	string1= (c1[0] + " "  + c1[1] + " "  + c1[2] + " "  + c1[3] + " "  + c1[4] 
				+ " "  + c1[5] + " "  + c1[6] + " "  + c1[7] + " "  + c1[8] + " "  + c1[9] + " "  
				+ c1[10] + " "  + c1[11] + " "  + c1[12] + " "  + c1[13] + " " + str(vsorted[0,0]) + " " 
				+ str(vsorted[0,1]) + " " + str(vsorted[0,2]) + " " + str(s1) + " " + str(s2) + " " + str(s3) 
				+ " " + str(shearOCT) + " "
				+ str(vsorted[1,0]) + " " + str(vsorted[2,0]) + " " + str(vsorted[3,0]) + " " 
				+ str(vsorted[1,1]) + " " + str(vsorted[2,1]) + " " + str(vsorted[3,1]) + " " 
				+ str(vsorted[1,2]) + " " + str(vsorted[2,2]) + " " + str(vsorted[3,2]) + " " + "\n")
	fb.write(string1)
	


