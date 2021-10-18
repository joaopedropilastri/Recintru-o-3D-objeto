from numpy import *
from math import e
from vpython import *
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import time

#pegar os valores das posições
c1=[]
c1= input("Digite as cordenadas X,Y,Z da camera 1 em sequencia(X Y Z) por favor use . para decimais no lugar de , :").split(" ")
print(c1)
pc1=[]
pc1= input("Digite as cordenadas X,Y,Z do ponto de projeção da camera 1 em sequencia(X Y Z) por favor use . para decimais no lugar de , :").split(" ")
print(pc1)
c2=[]
c2= input("Digite as cordenadas X,Y,Z da camera 2 em sequencia(X Y Z) por favor use . para decimais no lugar de , :").split(" ")
print(c2)
pc2=[]
pc2= input("Digite as cordenadas X,Y,Z do ponto de projeção da camera 2 em sequencia(X Y Z) por favor use . para decimais no lugar de ,:").split(" ")
print(pc2)

#variaveis de coeficiente para camera 1 e 2
mr1=[]
mr2=[]
br1=[]
br2=[]

mr1.append((float(pc1[1])-float(c1[1]))/(float(pc1[0])-float(c1[0])))
mr1.append((float(pc1[2])-float(c1[2]))/(float(pc1[0])-float(c1[0])))
mr1.append((float(pc1[1])-float(c1[1]))/(float(pc1[2])-float(c1[2])))

mr2.append((float(pc2[1])-float(c2[1]))/(float(pc2[0])-float(c2[0])))
mr2.append((float(pc2[2])-float(c2[2]))/(float(pc2[0])-float(c2[0])))
mr2.append((float(pc2[1])-float(c2[1]))/(float(pc2[2])-float(c2[2])))


br1.append(-1*(float(mr1[0])*float(c1[0])-float(c1[1])))
br1.append(-1*(float(mr1[1])*float(c1[0])-float(c1[2])))
br1.append(-1*(float(mr1[2])*float(c1[2])-float(c1[1])))

br2.append(-1*(float(mr2[0])*float(c2[0])-float(c2[1])))
br2.append(-1*(float(mr2[1])*float(c2[0])-float(c2[2])))
br2.append(-1*(float(mr2[2])*float(c2[2])-float(c2[1])))

#variaveis para contrução de x,y,z parciais do objeto procurado
xtemp=[]
ytemp=[]
xyzfim=[]

xtemp.append((-1*(float(mr2[0])*float(c2[0]))+float(c2[1])+(float(mr1[0])*float(c1[0]))-float(c1[1]))/(float(mr1[0])-float(mr2[0])))
xtemp.append((-1*(float(mr2[1])*float(c2[0]))+float(c2[2])+(float(mr1[1])*float(c1[0]))-float(c1[2]))/(float(mr1[1])-float(mr2[1])))
xtemp.append((-1*(float(mr2[2])*float(c2[2]))+float(c2[1])+(float(mr1[2])*float(c1[2]))-float(c1[1]))/(float(mr1[2])-float(mr2[2])))

ytemp.append((float(mr1[0])*float(xtemp[0]))-(float(mr1[0])*float(c1[0]))+float(c1[1]))
ytemp.append((float(mr1[1])*float(xtemp[1]))-(float(mr1[1])*float(c1[0]))+float(c1[2]))
ytemp.append((float(mr1[2])*float(xtemp[2]))-(float(mr1[2])*float(c1[2]))+float(c1[1]))

#recontrução 3d da posição do objeto procurado
rec3d=[]
rec3d.append((xtemp[0]+xtemp[1])/2)
rec3d.append((ytemp[0]+ytemp[2])/2)
rec3d.append((ytemp[1]+xtemp[2])/2)

print("valor da posição do objeto a partir da reconstrução 3d: ", rec3d)




    