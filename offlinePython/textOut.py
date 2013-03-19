"""


   w = 4
????????
?  ||  ?
? x||x ?
?--xx--?
? x||x ?
????????



  oo
 o  o
o    o
 o  o
  oo



"""







def presetBoard():

    board = ["BW---",
              "BW---",
              "BB---",
              "-WW--",
              "W-WW-"]
    w, n = 10, 5
    
    for i in range(len(board)):
        board[i] = listify(board[i])

    for lst in board:
        for i in range(len(lst)):
            lst[i] = stone(lst[i])

    return drawBoard(board,w,n)


def drawBoard(board,w,n):



    board = transpose(board)

# Build board of cell points
    p_Board = []

    p_Row = []
    p_Row.append(returnCell(w,("Top","Left"),board[0][0]))
    for i in range(n-2):
        p_Row.append(returnCell(w,("Top", "Centre"),board[0][i+1]))
    p_Row.append(returnCell(w,("Top","Right"),board[0][n-1]))
    p_Board.append(p_Row)

    for i in range(n-2):
        p_Row = []
        p_Row.append(returnCell(w,("Centre","Left"),board[i+1][0]))
        for j in range(n-2):
            p_Row.append(returnCell(w,("Centre", "Centre"),board[i+1][j+1]))
        p_Row.append(returnCell(w,("Centre","Right"),board[i+1][n-1]))
        p_Board.append(p_Row)

    p_Row = []
    p_Row.append(returnCell(w,("Bottom","Left"),board[n-1][0]))
    for i in range(n-2):
        p_Row.append(returnCell(w,("Bottom", "Centre"),board[n-1][i+1]))
    p_Row.append(returnCell(w,("Bottom","Right"),board[n-1][n-1]))
    p_Board.append(p_Row)
        
# extract list of row strings from p_Board


    s_Board = []
    
    for p_row in p_Board:
        for i in range(w):
            s_row = ""
            for p_point in p_row:
                s_row = s_row + p_point[i]
            s_Board.append(s_row)

    return s_Board

    
def stone(s):
    if s == "B":
        return "Black"
    if s == "W":
        return "White"
    if s == "-":
        return "Empty"
    a = 1/0


def returnCell(w,edge,stone):
    """
Returns a (w+1 length) list of (w+2 length) row strings.
-------------------
w = width of stone
edge = tuple describing where the cell is on the board e.g. ("Top","Centre") or ("Centre","Left")
point = the stone value of the cell, i.e. "Black", "White" or "Empty"
-------------------
First creates a list of row lists for an empty point.

Then fills in stone if required.

    """

    H = "-"
    V = "|"
    N = " "
    O = "o"
    X = "x"

    
    
    if edge[0] == "Top":
        a_V = N
        b_V = V
    elif edge[0] == "Centre":
        a_V = V
        b_V = V
    elif edge[0] == "Bottom":
        a_V = V
        b_V = N
    else:
        a = 1/0


    if edge[1] == "Left":
        l_H = N
        r_H = H
    elif edge[1] == "Centre":
        l_H = H
        r_H = H
    elif edge[1] == "Right":
        l_H = H
        r_H = N
    else:
        a = 1/0


# Row Strings
    abvStr = (w/2)*N   + 2*a_V + (w/2)*N
    cntStr = (w/2)*l_H + 2*H   + (w/2)*r_H
    blwStr = (w/2)*N   + 2*b_V + (w/2)*N
# Create standard cell
    rows = [abvStr]
    for i in range(w/2-1):
        rows.append(abvStr)
    rows.append(cntStr)
    for i in range(w/2-1):
        rows.append(blwStr)

# listify row strings so they can be edited

    for i in range(len(rows)):
        rows[i]=listify(rows[i])
        


# Put in o for black
    if stone == "Black":
        for i in range(w/2):
            rows[w/2+i][1+i] = "o"
            rows[w/2-i][1+i] = "o"
            rows[w/2+i][-2-i] = "o"    
            rows[w/2-i][-2-i] = "o"
# Put in x for white
    elif stone == "White":
        for i in range(w/2):
            rows[w/2+i][w/2+i+1] = "x"
            rows[w/2+i][w/2-i] = "x"
            rows[w/2-i][w/2+i+1] = "x"    
            rows[w/2-i][w/2-i] = "x"


# re-stringify listified row strings    

    for i in range(len(rows)):
        rows[i] =stringify(rows[i])



    return rows



def listify(str):
    lst = []
    for c in str:
        lst.append(c)
    return lst

def stringify(lst):
    str = ""
    for c in lst:
        str = str + c
    return str
    
def printBoard(board,w,n):
    str = ""
    for row in drawBoard(board,w,n):
        str = str + row + '\n'
    print str
    
def transpose(matrix):
    new_matrix = []
    for col in range(len(matrix)):
        new_row = []
        for row in range(len(matrix[col])):
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)
    return new_matrix
