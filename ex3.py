import pandas as pd
from random import shuffle as sf
from random import randint as rd
import math
import matplotlib.pyplot as plt

f= open("C:/Users/Capp/Documents/Università/Magistrale/1-ADM/Homework4/wine.data","r")
df=pd.DataFrame(f,columns=['chara'])
l=[]
for row in df['chara']:
    l.append(row.strip('\n').split(','))
    
xy=[]  #A list containing all points pf the scatter plot (Ash, Alcanity of ash)
for el in l:
    p=[]
    p.append(float(el[4]))
    p.append(int(el[5]))
    xy.append(p)
sf(xy)

plt.figure(figsize=(20,10))
for el in xy:
    plt.scatter(el[0],el[1], c='black')
plt.title('WINES',fontsize=30)
plt.xlabel('Ash',fontsize=20)
plt.ylabel('Alcalinity of ash',fontsize=20)
plt.show()


def dist(x,y):
    distance=math.sqrt(sum([(a-b)**2 for a,b in zip(x,y)])) #Euclidean distance
    return distance

#initialization first cluster center
c1=[rd(1,30),rd(1,170)]
#initialization second cluster center
c2=[rd(1,30),rd(1,170)]
iter=0
def kmean(c1,c2,iter):
    if iter!=5:
        clus=[c1,c2]
        clu={'c1':[],'c2':[]}  #A dictionary that groupify the points according to the clusters
        for i in range(len(xy)):
            distances=[]
            for el in clus:
                distances.append(dist(xy[i],el))
            if distances[0]==min(distances):
                clu['c1'].append(xy[i])
            else:
                clu['c2'].append(xy[i])
                
        #updating scatterplot
        plt.figure(figsize=(20,10))
        plt.scatter(c1[0],c1[1], c='g',marker='X',linewidths=10)
        plt.scatter(c2[0],c2[1], c='g',marker='X',linewidths=10)
        for el in xy:
            if el in clu['c1']:
                plt.scatter(el[0],el[1], c='r',marker='o')
            elif el in clu['c2']:
                plt.scatter(el[0],el[1], c='b',marker='o')
        plt.title('WINES',fontsize=30)
        plt.xlabel('Ash',fontsize=20)
        plt.ylabel('Alcalinity of ash',fontsize=20)
        
        #updating clusters
        c1x=[]
        c1y=[]
        for el in clu['c1']:
            c1x.append(el[0])
            c1y.append(el[1])
        
        c2x=[]
        c2y=[]
        for el in clu['c2']:
            c2x.append(el[0])
            c2y.append(el[1])
            
        try:
            c1=[round(sum(c1x)/len(c1x),3),round(sum(c1y)/len(c1y),3)]
            c2=[round(sum(c2x)/len(c2x),3),round(sum(c2y)/len(c2y),3)]
        except ZeroDivisionError:
            pass
        
        #updating iter
        iter+=1
        
        return plt.show(),kmean(c1,c2,iter)
    else:
        return print(c1,c2),plt.show()
kmean(c1,c2,iter)
