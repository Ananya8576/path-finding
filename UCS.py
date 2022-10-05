import sys
import heapq

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self,pos,rows,cols,board):
        self.pos=pos
        self.cols=cols
        self.rows=rows
        self.board=board
    
    #get the col (num)
    def get_c(self):
        return self.pos[1]
    
    #get the row (num)
    def get_r(self):
        return self.pos[0]
 
#finding threat area particluar to each piece  
class Rook(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        rook_moves=[]
        r,c=self.pos
        for i in range(r-1,-1,-1):
            if self.board[i,c]==-1:
                break
            else:
                if c<self.cols and c>=0:
                    rook_moves.append((i,c))
                continue
        for j in range(r+1,self.rows):
            if self.board[j,c]==-1:
                break
            else:
                if c<self.cols and c>=0:
                    rook_moves.append((j,c))
                continue
        for k in range(c+1,self.cols):
            if self.board[r,k]==-1:
                break
            else:
                if r<self.rows and r>=0:
                    rook_moves.append((r,k))
                continue
        for l in range(c-1,-1,-1):
            if self.board[r,l]==-1:
                break
            else:
                if r<self.rows and r>=0:
                    rook_moves.append((r,l))
                continue
        return rook_moves                
 
class Bishop(Piece):
  def __init__(self,pos,rows,cols,board):
    super().__init__(pos,rows,cols,board)
  
  def moves(self):
    r,c=self.pos
    bishop_moves=[]
    diag1 = zip(range(r+1,self.rows), range(c-1,-1,-1))
    diag2 = zip(range(r+1,self.rows), range(c+1,self.cols)) 
    diag3 = zip(range(r-1,-1,-1), range(c-1,-1,-1))
    diag4 = zip(range(r-1,-1,-1), range(c+1,self.cols))
    for r1,c1 in diag1:
        if r1<self.rows and r1>=0 and c1<self.cols and c1>=0:
            if self.board[r1,c1]==-1:
                break
            else:
                bishop_moves.append((r1,c1))
        else:
            continue
    for r2,c2 in diag2:
        if r2<self.rows and r2>=0 and c2<self.cols and c2>=0:
            if self.board[r2,c2]==-1:
                break
            else:
                bishop_moves.append((r2,c2))
        else:
            continue
    for r3,c3 in diag3:
        if r3<self.rows and r3>=0 and c3<self.cols and c3>=0:
            if self.board[r3,c3]==-1:
                break
            else:
                bishop_moves.append((r3,c3))
        else:
            continue
    for r4,c4 in diag4:
        if r4<self.rows and r4>=0 and c4<self.cols and c4>=0:
            if self.board[r4,c4]==-1:
                break
            else:
                bishop_moves.append((r4,c4))
        else:
            continue
    return bishop_moves
    
class Queen(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        queen_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.board)
        piece2=Bishop(self.pos, self.rows, self.cols,self.board)
        queen_moves.extend(piece1.moves())
        queen_moves.extend(piece2.moves())
        return queen_moves
    
class Knight(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self): #fixed 8 moves around piece
        op1=[-2,1,-1,2,2,1,-1,-2] #for row movement
        op2=[1,2,2,1,-1,-2,-2,-1] #for col movement
        knight_moves=[]
        r,c=self.pos
        for index in range(0,8):
            if r+op1[index]< self.rows and r+op1[index]>=0 and c+op2[index]<self.cols and c+op2[index]>=0:
                if self.board[r+op1[index],c+op2[index]]!=-1:
                    knight_moves.append((r+op1[index],c+op2[index]))
                else:
                    continue
            else:
                continue
        return knight_moves
 
class King(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        king_moves=[]
        r,c=self.pos
        for i in range(-1,2):
            for j in range(-1,2):
                if r+i<self.rows and c+j<self.cols and r+i>=0 and c+j>=0:
                    if (r+i,c+j)!=(r,c) and self.board[r+i,c+j]!=-1:
                        king_moves.append((r+i,c+j))
                    else:
                        continue
                else:
                    continue
        return king_moves
 
class Ferz(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        ops=[-1,1]
        ferz_moves=[]
        r,c=self.pos
        for i in ops:
            for j in ops:
                if r+i<self.rows and r+i>=0 and c+j<self.cols and c+j>=0:
                    if self.board[r+i,c+j]!=-1:
                        ferz_moves.append((r+i,c+j))
                    else:
                        continue
                else:
                    continue
        return ferz_moves
 
class Princess(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        princess_moves=[]
        piece1=Bishop(self.pos,self.rows, self.cols,self.board)
        piece2=Knight(self.pos, self.rows, self.cols, self.board)
        princess_moves.extend(piece1.moves())
        princess_moves.extend(piece2.moves())
        return princess_moves
    
class Empress(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        empress_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.board)
        piece2=Knight(self.pos, self.rows, self.cols,self.board)
        empress_moves.extend(piece1.moves())
        empress_moves.extend(piece2.moves())
        return empress_moves 
 
############################################################################
######## Board
#############################################################################
class Board:
    def __init__(self,r,c):
        self.r=r
        self.c=c
 
    def create_board(self,grid):
        dic = {}
        for i,val in enumerate(grid):
            for j,val2 in enumerate(val):
                dic[i,j]=val2
        return dic
            
#############################################################################
######## State
#############################################################################
class State:
    def __init__(self,pos,cost):
        self.pos=pos
        self.cost=cost

    def is_goal(self,goals):
        if self.pos in goals:
            return True
        else:
            return False

    def __lt__(self,other):
        if self.cost <= other.cost:
            return True
        return False

#############################################################################
######## Implement Search Algorithm
#############################################################################

def search(rows, cols, grid, enemy_pieces, own_pieces, goals):
    if rows==1 and cols==1:
        return ([],0)

    begin=own_pieces[0][1]

    board=Board(rows,cols)
    board=board.create_board(grid) #marking board with static obstacles (-1)
    board=enemy(board,enemy_pieces,own_pieces) #marking enemy positions as obstacles (-1)
    board=threat_area(board,enemy_pieces,rows,cols) #marking threat areas of enemy pieces as illegeal (-1)

    frontier=[]
    reached=set(begin)
    parent={}

    frontier.append(State(begin,0))
    parent[begin]= None

    final=False

    while len(frontier)>0 and final==False:
        v=heapq.heappop(frontier)
        current=v.pos
        cos=v.cost
        if current in goals:
            final=True
            tot=cos
            break
        else:
            for nex in valid_neighbors(board,current,rows,cols):
                u=nex.pos
                weight=nex.cost
                if u not in reached and u not in parent:
                    parent[u]=current
                    heapq.heappush(frontier, State(u,cos+weight))
                    reached.add(u)    
                else:
                    continue   
    if final==True:
        path=[]
        while parent[current]!= None:
            succ=(convert_to_char(current[1]),current[0])
            prev=(convert_to_char(parent[current][1]),parent[current][0])
            path.append([prev,succ])
            current = parent[current]
        path.reverse()
        return path,tot
    else:
        return ([],0)
 
def valid_neighbors(board,current,rows,cols):
    next = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
    res=[]
    r,c=current
    for d1,d2 in next:
        next_r,next_c= r+d1,c+d2
        if next_r>=0 and next_r<rows and next_c>=0 and next_c<cols and board[next_r,next_c]!= -1:
            res.append(State((next_r, next_c),board[next_r,next_c]))
        else:
            continue
    res.sort(key=lambda x: x.cost, reverse=False)
    return res

def threat_area(board,enemy_pieces,rows,cols):
    threat_area=[]
    if enemy_pieces!=[]:
        for name,pos in enemy_pieces:
            if name=='Rook':
                threat_area.extend(Rook(pos,rows,cols,board).moves())
            elif name=='Bishop':
                threat_area.extend(Bishop(pos,rows,cols,board).moves())
            elif name=='Queen':
                threat_area.extend(Queen(pos,rows,cols,board).moves())
            elif name=='Knight':
                threat_area.extend(Knight(pos,rows,cols,board).moves())
            elif name=='Ferz':
                threat_area.extend(Ferz(pos,rows,cols,board).moves())
            elif name=='Princess':
                threat_area.extend(Princess(pos,rows,cols,board).moves())
            elif name=='Empress':
                threat_area.extend(Empress(pos,rows,cols,board).moves()) 
            else:
                threat_area.extend(King(pos,rows,cols,board).moves())
        for (i,j) in set(threat_area):
            board[i,j]=-1
        return board
    else:
        return board
    #return set(threat_area)
 
def enemy(board, enemy_pieces,own_pieces):
    all=enemy_pieces+own_pieces
    names=[]
    for name,(pos1,pos2) in all:
        board[pos1,pos2]=-1
        names.append(name)
    return board
 
#converting num to char 
def convert_to_char(n):
    return chr(n + 97)

#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    grid = [[1 for j in range(cols)] for i in range(rows)] # Dictionary, label empty spaces as 1 (Default Step Cost)
    enemy_pieces = [] # List
    own_pieces = [] # List
    goals = [] # List

    handle.readline()  # Ignore number of obstacles
    for ch_coord in get_par(handle.readline()).split():  # Init obstacles
        r, c = from_chess_coord(ch_coord)
        grid[r][c] = -1 # Label Obstacle as -1

    handle.readline()  # Ignore Step Cost header
    line = handle.readline()
    while line.startswith("["):
        line = line[1:-2].split(",")
        r, c = from_chess_coord(line[0])
        grid[r][c] = int(line[1]) if grid[r][c] == 1 else grid[r][c] #Reinitialize step cost for coordinates with different costs
        line = handle.readline()
    
    line = handle.readline() # Read Enemy Position
    while line.startswith("["):
        line = line[1:-2]
        piece = add_piece(line)
        enemy_pieces.append(piece)
        line = handle.readline()

    # Read Own King Position
    line = handle.readline()[1:-2]
    piece = add_piece(line)
    own_pieces.append(piece)

    # Read Goal Positions
    for ch_coord in get_par(handle.readline()).split():
        r, c = from_chess_coord(ch_coord)
        goals.append((r, c))
    
    return rows, cols, grid, enemy_pieces, own_pieces, goals

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [piece, (r,c)]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: List of moves and nodes explored
def run_UCS():
    testcase = sys.argv[1]
    rows, cols, grid, enemy_pieces, own_pieces, goals = parse(testcase)
    moves, pathcost = search(rows, cols, grid, enemy_pieces, own_pieces, goals)
    return moves, pathcost
