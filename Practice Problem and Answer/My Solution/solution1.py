import numpy as np
import tqdm
from random import randint
import sympy
from random import shuffle


def read_collection(filename):
   
    lines = open(filename).readlines()
    N = [int(val) for val in lines[0].split()]
    piz = list(row.split() for row in lines[1:])
    n = N[0]
    return n, piz

photos =[]
#n, photos = read_collection('a_example.txt')
n, photos = read_collection('c_memorable_moments.txt')

HOS  = []
VERS = []
ALL = []
SCORE = 0
MAXSCORE = 0
COUPLE =[]
FINAL = []
'''
for i in range(n):
    if photos[i][0] == 'H':
        HOS.append([i]+photos[i])
    else:
        VERS.append([i]+photos[i])
'''
for i in range(n):
    ALL.append([i]+photos[i])
                               
print(ALL[0])

'''
for i in range(n-1):
    if ALL[i][1]=='H':
        FINAL.append(ALL[i][0])
    elif ALL[i][1]=='V':
        for j in range(i+1,n-1):
            #for k in range():
            SCORE = len(list(set(ALL[i][3:]) & set(ALL[j][3:])))
            if SCORE >= MAXSCORE:
                #del ALL[j]
                MAXSCORE = SCORE
                COUPLE = [ALL[i][0],ALL[j][0]]
            SCORE = 0

        FINAL.append(COUPLE)

print(i)
print(SCORE)
#print(len(list(set(ALL[1][3:]) & set(ALL[2][3:]))))
#print(FINAL[:100])
print(COUPLE)
'''
for i in range(n):
    if ALL[i][1]=='H':
        FINAL.append(ALL[i][0])

    elif ALL[i][1]=='V':
        for j in range(int(ALL[i][2])-1):
            print(ALL[i][j],sep="")
        
        
    



