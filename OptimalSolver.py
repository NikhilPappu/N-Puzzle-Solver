# USING PYTHON 3

import copy
import heapq
import NonOptimalSolver

def completed(l,n):
    for i in range(n):
        for j in range(n):
                if(l[i][j]!= 0 and l[i][j]!=i*n+j+1):
                    return 0
    return 1
def findZero(l,n):
    for i in range(n):
        for j in range(n):
            if (l[i][j] == 0):
                return (i, j)
def countInversions(initState):
    l = []
    inv = 0
    for i in initState.board:
        for j in i:
            l.append(j)
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]>l[j] and l[i]!=0 and l[j]!=0):
                inv+=1
    return inv
def checkSolvable(n,initState,goalState):
    (i,j) = findZero(initState.board,n)
    if(n%2!=0 and countInversions(initState)%2==0):
        solvable = True
    elif(n%2==0 and (n-(i+1))%2==0 and countInversions(initState)%2==0):
        solvable = True
    elif (n%2==0 and (n-(i+1))%2!= 0 and countInversions(initState)%2!=0):
        solvable = True
    else:
        solvable = False
    return solvable

class Board:
    def __init__(self,n,i,j):
        self.board = []
        self.moves = 0
        self.n = n
        self.prev = -1
        self.i = i
        self.j = j
        self.direction = -1
    def hamming(self):
        wrong = 0
        for i in range(self.n):
            for j in range(self.n):
                if(self.board[i][j]!=0 and self.board[i][j]!=self.n*i+j+1):
                    wrong+=1
        return wrong+self.moves
    def manhattan(self):
        d=0
        for i in range(self.n):
            for j in range(self.n):
                if(self.board[i][j]!=0):
                    x = (self.board[i][j]-1)//self.n
                    y = (self.board[i][j]-1)%self.n
                    d+=(abs(i-x)+abs(j-y))
        return d+self.moves

    def __lt__(self, other):
        return self.manhattan() < other.manhattan()

    def equals(self,state):
        for i in range(n):
            for j in range(n):
                if(self.board[i][j]!=state.board[i][j]):
                    return 0
        return 1
    def neighbours(self):
        l = []
        if(self.i>0):
            if(self.prev==-1 or self.direction!="d"):
                adj1 = Board(self.n, self.i - 1, self.j)
                adj1.board = copy.deepcopy(self.board)
                adj1.board[self.i][self.j], adj1.board[self.i - 1][self.j] = adj1.board[self.i - 1][self.j], \
                                                               adj1.board[self.i][self.j]
                adj1.prev = self
                adj1.moves = self.moves + 1
                adj1.direction = "u"
                l.append(adj1)
        if(self.i<self.n-1):
            if (self.prev == -1 or self.direction != "u"):
                adj2 = Board(self.n, self.i + 1, self.j)
                adj2.board = copy.deepcopy(self.board)
                adj2.board[self.i][self.j], adj2.board[self.i + 1][self.j] = adj2.board[self.i + 1][self.j], \
                                                                             adj2.board[self.i][self.j]
                adj2.prev = self
                adj2.moves = self.moves + 1
                adj2.direction = "d"
                l.append(adj2)
        if(self.j>0):
            if (self.prev == -1 or self.direction != "r"):
                adj3 = Board(self.n, self.i, self.j - 1)
                adj3.board = copy.deepcopy(self.board)
                adj3.board[self.i][self.j], adj3.board[self.i][self.j - 1] = adj3.board[self.i][self.j - 1], \
                                                                             adj3.board[self.i][self.j]
                adj3.prev = self
                adj3.moves = self.moves + 1
                adj3.direction = "l"
                l.append(adj3)
        if(self.j<self.n-1):
            if (self.prev == -1 or self.direction != "l"):
                adj4 = Board(self.n, self.i, self.j + 1)
                adj4.board = copy.deepcopy(self.board)
                adj4.board[self.i][self.j], adj4.board[self.i][self.j + 1] = adj4.board[self.i][self.j + 1], \
                                                                             adj4.board[self.i][self.j]
                adj4.prev = self
                adj4.moves = self.moves + 1
                adj4.direction = "r"
                l.append(adj4)
        return l

def nonOptimalSolver():
    for i in initState.board:
        for j in i:
            if(j<10):
                print(j,end = "  ")
            else:print(j,end=" ")
        print()
    print()
    board2 = NonOptimalSolver.solve(initState.board, n)
    if(n>3):
        l = []
        for i in board2:
            for j in i:
                l.append(j)
        l.sort()
        for i in range(3):
            for j in range(3):
                board2[i][j] = l.index(board2[i][j])
        initState2 = Board(3,0,0)
        initState2.board = copy.deepcopy(board2)
        (i,j) = findZero(initState2.board,3)
        initState2.i = i
        initState2.j = j
        initState2.n = 3
        del goalState.board
        goalState.board = [[1,2,3],[4,5,6],[7,8,0]]
        print("Running optimal solver on the 3x3...\n")
        optimalSolver(3,True,initState2,[])
        for a in moveList:
            (zi,zj) = findZero(initState.board,n)
            if(a=="u"):
                NonOptimalSolver.swap(initState.board,zi,zj,zi-1,zj)
            elif(a=="d"):
                NonOptimalSolver.swap(initState.board, zi, zj, zi + 1, zj)
            elif(a=="r"):
                NonOptimalSolver.swap(initState.board, zi, zj, zi, zj+1)
            elif(a=="l"):
                NonOptimalSolver.swap(initState.board, zi, zj, zi, zj-1)
        (zi,zj) = findZero(initState.board,n)
        NonOptimalSolver.swap(initState.board,zi,zj,initState.n-1,initState.n-1)
        print("Number of moves =",NonOptimalSolver.getCount())

def optimalSolver(n,second,initState,boardArray):
    heapq.heappush(boardArray,initState)
    while(completed(boardArray[0].board,n)!=1):
        for i in heapq.heappop(boardArray).neighbours():
            heapq.heappush(boardArray,i)
        if(second==False):
            if (len(boardArray) > 15000):
                print("Oops! The optimal solver is taking too long to compute.\nSwitching to non optimal solver...")
                nonOptimalSolver()
                return
    start = heapq.heappop(boardArray)
    path = []
    while(start.prev!=-1):
        path.append(start.prev.board)
        moveList.append(start.prev.direction)
        start = start.prev
    path.reverse()
    moveList.reverse()
    path.append(goalState.board)
    del moveList[0]
    if(second==False):
        print("The optimal solver ran fast enough. \nThe move set which takes the least number of moves is :\n")
        for i in path:
            for j in i:
                for z in j:
                    print(z,end=" ")
                print()
            print()
        print("Number of moves =",len(path)-1)

n = eval(input("Enter the size of the n-puzzle : \nn = "))
print("\nEnter the initial state of the board :")

initState = Board(n,0,0)
goalState = Board(n,0,0)
for i in range(n):
    initState.board.append([int(temp) for temp in input().strip().split()])
(i,j) = findZero(initState.board,n)
initState.i = i
initState.j = j
moveList = []
for i in range(n):
    goalState.board.append([j for j in range(n*i+1,n*(i+1)+1)])
goalState.board[n-1].remove(n**2)
goalState.board[n-1].append(0)

if(checkSolvable(n,initState,goalState)):
    if(n>3):
        ans = input("Enter O to use the optimal solver and NO to use the non optimal solver :\n")
    else:
        ans = "o"
        print("Automatically running the optimal solver because you entered a 3x3 puzzle...")
    if(ans.lower() == "o"):
        print("Using optimal solver...")
        optimalSolver(n,False,initState,[])
    elif(ans.lower()=="no"):
        print("Using non optimal solver...")
        nonOptimalSolver()
else:
    print("\nNo Solution")
    print("The solved state cannot be reached from the given initial state.")