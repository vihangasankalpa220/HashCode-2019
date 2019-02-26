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

#with open("b_small.in", "r") as ins:
#with open("a_example.in", "r") as ins:
with open("b_small.in", "r") as ins:
#with open("d_big.in", "r") as ins:
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
        
##print(array)
##print(data)
R = int(data[0])
C = int(data[1])
MIN = int(data[2])
MAX = int(data[3])
print(R,C,MIN,MAX)

try:
    #R,C,MIN,MAX = map(int,input().split())
    
    #pizza = [None]*R
    '''
    for i in range(0,R):
        pizza[i] = list(map(str, input().strip()))
        if len(pizza[i])!= C:
            break;
     '''
    pizza=array
    print(pizza)
    ##------transpose
    '''
    transpose = [[0 for x in range(C)] for y in range(R)]
    print(transpose)
    for i in range(0,R-1):
       for j in range(0,C):
           transpose[j][i] = pizza[i][j]
    '''
    transpose = [list(i) for i in zip(*pizza)]
    print(transpose)
    
    def countElement(lst, x): 
        count = 0
        for ele in lst: 
            if (ele == x): 
                count = count + 1
        return count
            
    def isBallenced(array):
        if MIN <= countElement(array, 'T') and MIN <= countElement(array, 'M'):
            return 1
        else:
            return 0
    print(countElement(transpose[0],'M'))   
    print(isBallenced(transpose[0]))

    flag = 0
    ranges = []
    for x in range(0,R):
            if isBallenced(pizza[x])==1:
                ranges.append(x)
    print(ranges)


            
    
except:
    print("Error!")
    

##Mushroom -> M | Tomato -> T


