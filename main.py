# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:23:43 2022

@author: sacha
"""
import integration as ig
from mpl_toolkits import mplot3d
import numpy as np, matplotlib.pyplot as plt

import math
import csv
plt.close()
plt.close()
plt.close()
plt.close()
chemin = ig.fct_parcourir()
ig.removeheader(chemin)
data = open("Data.csv",'r')
reader = csv.reader(data, delimiter=',')
t=[]
gz=[]
gx=[]
gy=[]
n=[]
for col in reader: #Dans cette boucle, on sépare le fichier csv en listes correspondantes aux colonnes (temps, accélération en x,y,z, norme)
     t.append(float(col[0])) #n°0 = 1ére colonne
     gx.append(float(col[1])) #n°1 = 2eme colonne
     gy.append(float(col[2])) #n°2 = 3eme colonne
     gz.append(float(col[3])) 
     n.append(float(col[4]))

#On calcul la moyenne de chaque tableau d'accélération sur une période où on est censés être immobiles et on enlève a tous les points des
     #tableaux cette valeur. 
moygx=ig.moyenne(0,10,gx)
moygy=ig.moyenne(0,10,gy)
moygz=ig.moyenne(0,10,gz)
'''for i in range(0,len(t)-1):
    gx[i]=gx[i]-moygx
    gy[i]=gy[i]-moygy
    gz[i]=gz[i]-moygz    ''' 
    
     
#On calcul les vitesses et les positions selon les 3 axes
tint,vz=ig.rectangle(t,gz,1)
tz2, z= ig.rectangle(tint, vz, 1)

tint2,vy=ig.rectangle(t,gy,1)
ty2,y=ig.rectangle(tint2,vy,1)

tint3,vx=ig.rectangle(t,gx,1)
tx2,x=ig.rectangle(tint3,vx,1)


#On calcul la norme de la vitesse et on regarde si il y a un exces de vitesse
norme = ig.norme(t,vx,vy,vz)

#On calcul la norme de l'accélération et on regarde si le trajet est confortable ou pas
normeaccel=ig.norme(t,gx,gy,gz)


#On cherche le min et le max des trois tableaux pour fixer la limite des axes
up,down=ig.minmax(x, y, z)


#On trace le graph 3.gcca

ax = plt.figure().add_subplot(projection='3d')  # Affichage en 3D
ax.plot(x, y, z, label='Courbe', marker=".")  # Tracé de la courbe 3D
plt.title("Courbe 3D")
ax.set_xlim(down,up)
ax.set_ylim(down,up)
ax.set_zlim(down,up)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()
#On trace les accélérations et on calcul l'accélération de la pesanteur. 
plt.figure()
plt.plot(t,gx, label="gx(t)")
plt.plot(t,gy,label="gy(t)")
plt.plot(t,gz,label="gz(t)")
plt.legend()
plt.show()



data.close()
print("Bonjour")