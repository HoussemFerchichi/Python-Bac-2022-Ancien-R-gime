from random import randint
import numpy as np
SequenceArray = []
skippedindexes = []
SequeceIndex = 0

def fill():
    global mat,tab,n
    n = int(input("Provide Your Matrice Size: "))
    tab = np.array([int]*n)
    mat = []
    for i in range (n):
        mat.append([0]*n)
        for j in range(n):
            mat[i][j]= randint(-100,100)
    Split(n,tab,mat)

def Split(n,t,mat):
    for i in range (n):
        FillTable(t,i,n,mat)
    Save()

def FillTable(t,p,n,mat):
    for i in range (n):
        t[i] = mat[p][i]
    SearchSeq(n,t,p)


def SearchSeq(n,t,p):
    global SequeceIndex,SequenceArray
    for i in range (n-1):
        s = t[i]
        j = i
        Verif = True
        skippedindexes = []
        while Verif :
            j = j +1
            if (j>=n-1):
                Verif = False
            s = s+t[j]
            if (s == 0) and (not(j in skippedindexes)):
                SequenceArray.append(str(p)+ " " + str(i)+" "+str(j))
                skippedindexes.append(j)
                SequeceIndex = SequeceIndex + 1
                j = i
                s = t[i]
                Verif = True
def Save():
    global n,SequenceArray,SequeceIndex
    f = open("F.txt","w")
    f.write("Les séquences contigues des lignes \n")
    s = open("F.txt","a")
    for i in range (SequeceIndex):
        s.write(SequenceArray[i] + "\n")
    f.close()
    s.close()







fill()