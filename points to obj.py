import numpy as np
import scipy
import scipy.io as scio
from PIL import Image
import numpy.linalg as la

d=scio.loadmat("in/analysis/Synapses1_mem3_good3_maxdisp500_difflength4.mat")['Synapses1']
data=[]
for i in d:
    for j in i:
        for k in j:
            data.append([k[0],k[1],k[2]])
data=np.array(data)
v=[]
f=[]
#each point turns into a tetrahedron
pointA=np.array([0.0, 0.0, -1.0])
pointB=np.array([0.0, 0.942809, 0.333333])
pointC=np.array([-0.816497, -0.471405, 0.333333])
pointD=np.array([0.816497, -0.471405, 0.333333])
#how big arounds the points it is
size=50
#scale numbers down for better viewing
scale=10000
c=1
for i in data:
    #define verticies
    v.append((i+(pointA*size))/scale)
    v.append((i+(pointB*size))/scale)
    v.append((i+(pointC*size))/scale)
    v.append((i+(pointD*size))/scale)
    #define faces(tuples of vertecies)
    f.append(np.array([c,c+1,c+2]))
    f.append(np.array([c,c+2,c+3]))
    f.append(np.array([c,c+3,c+1]))
    f.append(np.array([c+3,c+2,c+1]))
    c+=4

textfile = open("out.obj", "w")
textfile.write("#obj write from points- Alex Nickl" + "\n")
for i in v:
    textfile.write("v  "+ str(i[0]) + ' ' + str(i[1]) + ' ' +str(i[2]) +"\n")
textfile.write("\n")
for i in f:
    textfile.write("f  "+ str(i[0]) + ' ' + str(i[1]) + ' ' +str(i[2]) +"\n")
textfile.close()
