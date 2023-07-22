from tkinter import *
from tkinter.filedialog import askopenfilename
import numpy as np, matplotlib.pyplot as plt
def fct_parcourir():#fonction pour obtenir le path du fichier de données 
    root=Tk()
    fichier=askopenfilename()
    print(fichier)
    root.destroy()
    root.mainloop()
    return fichier

def minmax(x,y,z):#On cherche le min et le max de l'accélération sur les 3 axes pour les limites des axes 
    up=[]
    down=[]
    up.append(max(x))
    up.append(max(y))
    up.append(max(z))
    down.append(min(x))
    down.append(min(y))
    down.append(min(z))
    plus = max(up)
    moins=min(down)
    return plus, moins

        

def removeheader(chemin):#fonction pour enlever la première ligne du fichier avec le nom des colonnes
    with open(chemin, "rb") as infile, open("Data.csv", "wb") as outfile:
       next(infile)  
       outfile.write(infile.read())
    return outfile

def norme(t,x,y,z):#On calcul la norme de l'accélération
  accel=[]
  for i in range (0,len(x)):
    module=(x[i]**2+y[i]**2+z[i]**2)**(1/2)
    accel.append(module)

  return accel
    
    
def rectangle(t,z,tau=1):
    aire=[]
    #a,b et h
    tint=[]
    inte=[]
    for i in range(0, len(z)-tau):
        air= (t[i+tau]-t[i])*z[i]
        aire.append(air)
        ti= t[i]+((t[i+tau]-t[i])/2)
        tint.append(ti)
    inte.append(aire[0])
    for k in range(1,len(tint)-1):
        integ=inte[k-1]+aire[k]
        inte.append(integ)
    inte.append(inte[-2])
    return tint,inte

def moyenne(depart,arrivee,g):
    somme=0
    k=depart*100
    l=arrivee*100
    for i in range(k,l-2):
        somme=somme+g[i]
    moyenne=somme/i
    return moyenne
        
def simpson(t,z, tau=1):
    aire=[]
    tint=[]
    inte=[]
    for i in range(0,len(z)-2*tau):
        ai=(((t[i+2*tau])-t[i])/6)*(z[i]+4*z[i+tau]+z[i+tau])
        aire.append(ai)
        ti= t[i]+((t[i+2*tau]-t[i])/2)
        tint.append(ti)
    inte.append(aire[0])
    for k in range(1,len(tint)-1):
        integ=inte[k-1]+aire[k]
        inte.append(integ)
    inte.append(inte[-1])
    return tint,inte

def trapeze(t,z,tau=1):
    aire=[]
    tint=[]
    inte=[]
    for i in range(0,len(z)-tau):
        #print(i)
        ai= ((z[i+tau]+z[i])/2)*(t[i+tau]-t[i])
        aire.append(ai)
        ti= t[i]+((t[i+tau]-t[i])/2)
        tint.append(ti)
    inte.append(aire[0])
    for k in range(1,len(tint)-1):
        integ=inte[k-1]+aire[k]
        inte.append(integ)
    inte.append(inte[-1])
    return tint, inte


def vartau(methode,t,z):
    plt.figure()
    if methode=="rectangle":
        for i in range(1,10,2):
            tint, vz= rectangle(t, z, i)
            plt.plot(tint,vz,label=i)
    if methode=="trapeze":
        for i in range(1,10,2):
            tint, vz= trapeze(t, z, i)
            plt.plot(tint,vz,label=i)
    if methode=="simpson":
        for i in range(1,10,2):
            tint, vz= simpson(t, z, i)
            plt.plot(tint,vz,label=i)
    plt.legend()
    plt.show()