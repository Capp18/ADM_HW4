#My counting sort is a checking of the list:
#if an element isn't in the right position related to the next one,
#it will be moved to the last position of the list
#until we have the right order.
#For example: list=[Nazanin,Dario,Wei] will be modified in [Dario,Wei,Nazanin] and then in [Dario,Nazanin,Wei]

#LETTERS SORTING

l=list(map(str,input().split()))
for k in range(len(l)):
    l[k]=l[k].lower()
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

##########################################################################################################

#WORDS SORTING

l=list(map(str,input().split()))
for k in range(len(l)):
    l[k]=l[k].lower()
#Using a dictionary, the algorithm assigns a value to each letter
alph={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,
      'g':6,'h':6,'i':7,'j':8,'k':9,'l':10,
      'm':11,'n':12,'o':13,'p':14,'q':15,'r':16,
      's':17,'t':18,'u':19,'v':20,'w':21,'x':22,'y':23,'z':24} 
def sortWords(l):
    l1=l[:]
#At every iteration of the recursive function,the algorithm check if each word's letter has an higher value than the next word's letter
    for i in range(len(l1)-1):
        for j in range(len(l1[i])):
            try:
                if alph[l1[i][j]]>alph[l1[i+1][j]]:  #If it happens, the word is moved to the last position of the list
                    l1.append(l1[i])
                    l1.remove(l1[i])
                    break
                elif alph[l1[i][j]]<alph[l1[i+1][j]]: #if it doesn't happen, the algo pass to the next word
                    break
                else:
                    pass          #If the values are equal, the algo pass to the next letter
            except IndexError:
                pass
    res=1    
    for j in range(len(l)):
        if l[j]!=l1[j]:
            res=0
            break
    if res==0:
        l=l1[:]  #If the sorted list is different from the starting one, the function repeats the operations with the new list!
        return sortWords(l) 
    elif res==1:
        return print(l1)   #If the sorted list is equal to the starting one, the algorithm stops!
sortWords(l)
