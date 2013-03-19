
def play(state,(x,y)):
    output = state.board.play(state.player,state.captured,(x,y))
    if output[0] == 0:
        if state.player == "Black":
            state.player = "White"
        else: state.player = "Black"

    return state

class go_board:
    """
Initialising creates an nxn board.

Interact with a board by:
* attempting to place a stone using self.play(player, (x,y)):
    - Only valid moves will go ahead.
    - Non-valid moves will return a tuple of -1 and
    a short explanation of why the moves isn't valid
* passing with self.passMove()
* asking for a list output of the board's contents with self.output()
* setting the value of "self.printEveryMove" or calling a print with self.printNow()
* setting the width of stones in print outputs by changing self.w


    """
    
    def __init__(self,n):
        self.n = n
        self.values = {}
        
        for x in range(n):
            for y in range(n):
                self.values[(x,y)] = "Empty"

        self.lastValues = self.values.copy()
        self.lastLastValues = self.lastValues.copy()
        
    def __getitem__(self,(x,y)):
        return self.values[(x,y)]
    def __setitem__(self,(x,y), item):

        if item == "Empty" or item == "Black" or item == "White" or item =="Selected":
            self.values[(x,y)] = item
        else:
            a = 1/0
    def output(self):
        n = self.n
        board_out = []
        for y in range(n):
            row = []
            for x in range(n):
                row.append(self.values[(x,y)])
            board_out.append(row)
        return board_out
        
    def play(self, player, captured, (x,y)):
        
# Check player is valid
        if not (player == "Black" or player == "White"):
            return -1,"invalid player"

# Check point is empty
        if not self.values[(x,y)] == "Empty":
            return -1,"Non-empty point"

# Place stone
        self.values[(x,y)] = player


# Check each neighbour in turn
        for neighbour in self.getNeighbours((x,y)):
    # If a neighbour's group has no liberties, replace it with empty points           
            if not (neighbour[1] == "Empty"  or neighbour[1] == player):
                neighbourGroup = self.getGroup(neighbour[0])
                if len(self.getLiberties(neighbourGroup)) == 0:
                    for member in neighbourGroup:
                        captured[self.values[member]] += 1
                        self.values[member] = "Empty"
                    
            
# Check the group just added to has liberties, if not, remove stone from the board.
        if len(self.getLiberties(self.getGroup((x,y)))) == 0:
            self.values[(x,y)] = "Empty"
            return -1, "Cannot play to create a zero liberty group unless doing so will kill a neighbour and so create liberties"


# Check the board is not now in the state it was in two moves ago, if it is, undo the move.
        if self.values == self.lastLastValues:
            self.values = self.lastValues.copy()
            return -1, "You cannot instantly reply to a ko"
        else:
            self.lastLastValues = self.lastValues.copy()
            self.lastValues = self.values.copy()
            

        return 0, ""


    def passMove(self):
        self.lastLastValues = self.lastValues.copy()
        self.lastValues = self.values.copy()

    def getNeighbours(self, (x,y)):
        n = self.n
        lst = []
        if not x == 0:
            lst.append([(x-1,y),self.values[(x-1,y)]])
        if not x == n-1:
            lst.append([(x+1,y),self.values[(x+1,y)]])
        if not y == 0:
            lst.append([(x,y-1),self.values[(x,y-1)]])
        if not y == n-1:
            lst.append([(x,y+1),self.values[(x,y+1)]])
        return lst



    def getImmediateGroup(self, (x,y)):
        
        n = self.n
        player = self.values[(x,y)]
        
        if player == "Empty":
            return set([])
        lst = []
        for neighbour in self.getNeighbours((x,y)):
            if neighbour[1] == player:
                lst.append(neighbour[0])
            
        return set(lst)

    def getGroup(self,(x,y)):
        checkedGroup = set([])
        uncheckedGroup = set([])
        
        uncheckedGroup.add((x,y))
        while len(uncheckedGroup) > 0:
            unchecked_neighbours = set([])
            for point in uncheckedGroup:
                neighbours = self.getImmediateGroup(point)
                unchecked_neighbours.update(neighbours.difference(checkedGroup))
                checkedGroup.add(point)
            uncheckedGroup = unchecked_neighbours

        return checkedGroup
    
    def getLiberties(self,group):
        n = self.n
        
        liberties = set([])
        for point in group:
            x,y = point
            if not x == 0:
                if self.values[(x-1,y)] == "Empty":
                    liberties.add((x-1,y))
            if not x == n-1:
                if self.values[(x+1,y)] == "Empty":
                    liberties.add((x+1,y))
            if not y == 0:
                if self.values[(x,y-1)] == "Empty":
                    liberties.add((x,y-1))
            if not y == n-1:
                if self.values[(x,y+1)] == "Empty":
                    liberties.add((x,y+1))
        return liberties





