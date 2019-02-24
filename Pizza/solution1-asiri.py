##----------INPUT
##  3 rows, 5 columns, min 1 of each ingredient per slice, max 6 cells per slice
##  3 5 1 6
##  TTTTT
##  TMMMT
##  TTTTT

##---------output
##  3
##  0 0 2 1
##  0 2 2 2
##  0 3 2 4
##  3 slices.
##  First slice between rows (0,2) and columns (0,1).
##  Second slice between rows (0,2) and columns (2,2).
##  Third slice between rows (0,2) and columns (3,4).
'''
with open("b_small.txt", "r") as ins:
    array = []
    data = []
    y = 0
    for line in ins:
        x =[]
        if y ==0 :
            data = line.split()
        else:
            x = list(line.strip())
            array.append(x)
        y+=1
        
print(array)
print(data)
'''
try:
    R,C,MIN,MAX = map(int,input().split())
    
    pizza = [None]*C

    print(pizza)
    
    for i in range(0,R+1):
        pizza[i] = list(map(str, input().strip()))
        if len(pizza[i])> C:
            break;
           
    print(pizza)
except:
    print("Error!")
    

##Mushroom -> M | Tomato -> T


