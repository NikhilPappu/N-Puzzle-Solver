# USING PYTHON 3
count = 0

def find(a,l,n):
    for i in range(n):
        for j in range(n):
            if(l[i][j]==a):
                return (i,j)

def swap(l,r1,c1,r2,c2):
    global count
    l[r1][c1],l[r2][c2] = l[r2][c2],l[r1][c1]
    if(r1!=r2 or c1!=c2):
        count += 1
        for a in l:
            for b in a:
                if(b<10):
                    print(b, end="  ")
                else:
                    print(b,end=" ")
            print()
        print()
def getCount():
    global count
    return count
def manhattanDist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)
def shortestPath(r1,c1,r2,c2):
    path1 = []
    path2 = []
    R1 = r1
    C1 = c1
    if(r1>r2):
        while(r1>r2):
            path1.append((r1,c1))
            r1-=1
        if(c1>c2):
            while(c1>=c2):
                path1.append((r1,c1))
                c1-=1
        else:
            while(c2>=c1):
                path1.append((r1,c1))
                c1+=1
    else:
        while(r2>r1):
            path1.append((r1,c1))
            r1+=1
        if (c1 > c2):
            while (c1 >= c2):
                path1.append((r1, c1))
                c1 -= 1
        else:
            while (c2 >= c1):
                path1.append((r1, c1))
                c1 += 1
    r1 = R1
    c1 = C1
    if (c1 > c2):
        while (c1 > c2):
            path2.append((r1, c1))
            c1 -= 1
        if (r1 > r2):
            while (r1 >= r2):
                path2.append((r1, c1))
                r1 -= 1
        else:
            while (r2 >= r1):
                path2.append((r1, c1))
                r1 += 1
    else:
        while (c2 > c1):
            path2.append((r1, c1))
            c1 += 1
        if (r1 > r2):
            while (r1 >= r2):
                path2.append((r1, c1))
                r1 -= 1
        else:
            while (r2 >= r1):
                path2.append((r1, c1))
                r1 += 1


    return (path1,path2)
def moveBlank(dr,dc,val,row,board,n):
    newVal = val%n
    if(newVal==0):newVal=n
    (zi, zj) = find(0, board,n)
    (onei,onej) = find(val,board,n)
    bpath1 = shortestPath(zi, zj, dr, dc)[0]
    bpath2 = shortestPath(zi, zj, dr, dc)[1]
    if((onei,onej) not in bpath1 and (row,newVal-2) not in bpath1 and (row-1,newVal-1) not in bpath1):
        for i in bpath1:
            swap(board,zi,zj,i[0],i[1])
            zi=i[0]
            zj=i[1]
    elif((onei,onej) not in bpath2 and (row,newVal-2) not in bpath2 and (row-1,newVal-1) not in bpath2):
        for i in bpath2:
            swap(board,zi,zj,i[0],i[1])
            zi=i[0]
            zj=i[1]

def Up(i,j,val,row,board,n):
    moveBlank(i - 1, j,val,row,board,n)
    swap(board, i - 1, j, i, j)
def Left(i,j,val,row,board,n):
    moveBlank(i, j - 1,val,row,board,n)
    swap(board, i, j - 1, i, j)
def Right(i,j,val,row,board,n):
    moveBlank(i,j+1,val,row,board,n)
    swap(board,i,j+1,i,j)
def Down(i,j,val,row,board,n):
    moveBlank(i+1,j,val,row,board,n)
    swap(board,i+1,j,i,j)
def placeElement(val,row,board,n,col):
    newVal = val % n
    if (newVal == 0): newVal = n
    (i, j) = find(val, board,n)
    if(col==True):
        while(i<(val//n)+1 and val//n!=1):
            if(row==n-1 and i==val//n):break
            (zi, zj) = find(0, board, n)
            if(zj==j and zi<i):
                if(j<n-1):
                    swap(board,zi,zj,zi,zj+1)
                    zj+=1
                else:
                    swap(board,zi,zj,zi,zj-1)
                    zj-=1
            Down(i,j,val,row,board,n)
            i+=1
        if (row == n - 1):
            if (find(val, board, n)[0] != row or find(val, board, n)[1] != newVal - 1):
                placeColumnN(val, row, board, n)
            return
    while(j<newVal and newVal!=1):
        if(newVal==n and j==(newVal-1)):
            if((find(val, board,n)[0] != row or find(val, board,n)[1] != newVal - 1)):
                placeRowN(val,row,board,n)
            return
        (zi, zj) = find(0, board,n)
        if(zi==i and zj<j):
            if(i<n-1):
                swap(board,zi,zj,zi+1,zj)
                zi+=1
            else:
                swap(board,zi,zj,zi-1,zj)
                zi-=1
        Right(i,j,val,row,board,n)
        j+=1
    while (i > row and j > newVal-1):
        (zi, zj) = find(0, board,n)

        if(j==zj and zi>i):
            Left(i,j,val,row,board,n)
            j-=1
        elif(i==zi and zj>j):
            Up(i,j,val,row,board,n)
            i-=1
        elif(manhattanDist(zi,zj,i-1,j)<=manhattanDist(zi,zj,i,j-1)):
            Up(i, j,val,row,board,n)
            i -= 1
        elif(manhattanDist(zi,zj,i-1,j)>manhattanDist(zi,zj,i,j-1)):
            Left(i,j,val,row,board,n)
            j-=1
    while (i > row):
        (zi, zj) = find(0, board,n)
        if(zj==newVal-1 and zi>i):
            if(zj<n-1):
                swap(board,zi,zj,zi,zj+1)
                zj+=1
            else:
                swap(board,zi,zj,zi,zj-1)
                zj-=1
            Up(i,j,val,row,board,n)
            i-=1
        else:
            Up(i,j,val,row,board,n)
            i-=1
    while (j > newVal-1):
        (zi, zj) = find(0, board,n)

        if(zi==i and zj>j):
            swap(board,zi,zj,zi+1,zj)
            Left(i,j,val,row,board,n)
            j-=1
        else:
            Left(i,j,val,row,board,n)
            j-=1

def placeRowN(val,row,board,n):
    newVal = val % n
    if (newVal == 0): newVal = n
    (zi, zj) = find(0, board, n)
    (i, j) = find(val, board, n)
    if (zi == row and zj == n - 1 and i == row + 1 and j == n - 1):
        swap(board, zi, zj, i, j)
        return
    (i, j) = find(val, board, n)
    while (i > row + 1):
        (zi, zj) = find(0, board, n)
        if (zj == j and zi > i):
            swap(board, zi, zj, zi, zj - 1)
        Up(i, j, val, row, board, n)
        i -= 1
    moveBlank(i+1,j,val,row,board,n)
    swap(board,i,j,i+1,j)
    i-=1
    swap(board,row,n-1,row+1,n-1)
    swap(board,row,n-1,row,n-2)
    swap(board,row,n-2,row+1,n-2)
    swap(board,row+1,n-2,row+1,n-1)
    swap(board,row+1,n-1,row+2,n-1)
    swap(board,row+2,n-1,row+2,n-2)
    swap(board,row+2,n-2,row+1,n-2)
    swap(board,row+1,n-2,row,n-2)
    swap(board,row,n-2,row,n-1)
    swap(board,row,n-1,row+1,n-1)

def placeColumnN(val,row,board,n):
    newVal = val % n
    if (newVal == 0): newVal = n
    (zi, zj) = find(0, board, n)
    (i, j) = find(val, board, n)
    if(zi==n-1 and zj==newVal+1 and i==n-1 and j==newVal):
        swap(board,zi,zj,i,j)
        return
    (i, j) = find(val, board, n)
    while(j>newVal):
        (zi, zj) = find(0, board, n)
        if(zi==i and zj>j):
            swap(board,zi,zj,zi-1,zj)
        Left(i,j,val,row,board,n)
        j-=1
    moveBlank(i, j+1, val, row, board, n)
    swap(board, i, j, i, j+1)
    j-=1
    swap(board,n-1,newVal,n-1,newVal-1)
    swap(board,n-1,newVal-1,n-2,newVal-1)
    swap(board,n-2,newVal-1,n-2,newVal)
    swap(board,n-2,newVal,n-1,newVal)
    swap(board,n-1,newVal,n-1,newVal+1)
    swap(board,n-1,newVal+1,n-2,newVal+1)
    swap(board,n-2,newVal+1,n-2,newVal)
    swap(board,n-2,newVal,n-2,newVal-1)
    swap(board,n-2,newVal-1,n-1,newVal-1)
    swap(board,n-1,newVal-1,n-1,newVal)

def placeRow(row,board,n):
    for i in range(1,n+1):
        if (find(i, board,n)[0] != row or find(i, board,n)[1] != i - 1):
            placeElement(i+n*row,row,board,n,False)
def placeColumn(col,board,n):
    for i in range(1,n):
        if (find(col+i*n+1, board, n)[0] != i or find(col+i*n+1, board, n)[1] != col):
            placeElement(col+1+i*n,i,board,n,True)

def solve(board,n):
    for i in range(n-3):
        placeRow(i,board,n)
        placeColumn(i,board,n)
    if(n>3):
        new_list = [row[1:] for row in board[1:]]
        for i in range(n-4):
            new_list = [row[1:] for row in new_list[1:]]
        return new_list
    else: return board

