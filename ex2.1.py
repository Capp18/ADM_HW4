l=list(map(str,input().split()))
#Using a dictionary, the algorithm assigns a value to each letter
alph={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,
      'g':6,'h':6,'i':7,'j':8,'k':9,'l':10,
      'm':11,'n':12,'o':13,'p':14,'q':15,'r':16,
      's':17,'t':18,'u':19,'v':20,'w':21,'x':22,'y':23,'z':24} 
def sortChar(l):
    l1=l[:]
    #At every iteration of the recursive function,the algorithm check if each letter has an higher value than the next one
    for i in range(len(l1)-1):
        if alph[l1[i]]>alph[l1[i+1]]:  #If it happens, the letter is moved to the last position of the list
            l1.append(l1[i])
            l1.remove(l1[i])
            break
    
    res=1    
    for j in range(len(l)):
        if l[j]!=l1[j]:
            res=0
            break
    if res==0:
        l=l1[:]  #If the sorted list is different from the starting one, the function repeats the operations with the new list!
        return sortChar(l) 
    elif res==1:
        return print(l1)   #If the sorted list is equal to the starting one, the algorithm stops!
sortChar(l)
