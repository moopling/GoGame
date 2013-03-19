"""
hub.py recieves user inputs and intereprets them for rules.py.
rules.py then accordingly adjusts the game state which it returns to hub.py.
hub.py then sends the game state to graphicalOut.py, which draws the board for hub.py to then update.

gameState contains
-mode

-board
-n
-player
-captures
-passCount
-screenHeight


hub:

setupGame
- mode = "Setup"
- for now, in setup, don't interact with graphics, just do it through a shell

playGame
- mode = "Game"
- snap mouse
- handle clicks
- send to graphics








"""

import rules
import graphicalOut
import textOut



class gameState:
    def __init__(self):
        self.mode = "Setup"
        self.board = None
        self.n = None
        self.player = "Black"
        self.captured = {"Black":0,"White":0}
        self.passCount = 0
        self.screenHeight = 650
        self.textOut = False
        self.buttons = []
    def set_n(self,n):
        self.n = n
        self.board = rules.go_board(n)




def snapMouse(n,screenHeight,pos):
    delta = screenHeight/n
    if pos[0] >0 and pos[0] < n*delta and pos[1] >0 and pos[1] < n*delta:
        return (int(delta*(int(pos[0]/delta)+0.5)),int(delta*(int(pos[1]/delta)+0.5)+0.5))
    else:
        return pos


def onGrid(n,screenHeight,pos):
    delta = screenHeight/n
    if pos[0] >0 and pos[0] < n*delta and pos[1] >0 and pos[1] < n*delta:
            return True
    return False

def gridPosition(n,screenHeight,pos):
    delta = screenHeight/n
    return (int(pos[1]/delta),int(pos[0]/delta))


class button:
#a rectangular button        
    def __init__(self,text,(x,y),(w,h),colour ,function):
        self.text = text
        self.colour = colour
#position of top left corner                
        self.pos = (x,y)
        self.size = (w,h)
        self.function = function
        
    def changePos(self,newX=None,newY=None):
        if newX == None:
            newX = self.pos[0]
        if newY == None:
            newY = self.pos[1]
        self.pos = (newX,newY)
        
    def changeSize(self,newW=None,newH=None):
        if newW == None:
            newW = self.size[0]
        if newH == None:
            newH = self.size[1]
        self.pos = (newW,newH)
            
    def isOn(self,(x,y)):
        if x > self.pos[0] and x < self.pos[0] + self.size[0]:
            if y > self.pos[1] and y < self.pos[1] + self.size[1]:
                return True
        return False

    
def setupGame():

    state = gameState()


    
    if (raw_input("Test mode? ") == "Yes"):
        state.set_n(9)
        
        state.screenHeight = 650
        state.board.play("Black",state.captured,(1,0))
        state.board.play("Black",state.captured,(1,1))
        state.board.play("Black",state.captured,(1,2))
        state.board.play("Black",state.captured,(0,2))
        
        state.board.play("White",state.captured,(2,0))
        state.board.play("White",state.captured,(2,1))
        state.board.play("White",state.captured,(2,2))
        state.board.play("White",state.captured,(0,3))
        state.board.play("White",state.captured,(1,3))
        state.board.play("White",state.captured,(0,0))
        state.textOut = True

        state.mode = "Game"
        return state
            

    n = 0
    while n not in [5,9,13,19]:
        n = int(input("Pick a board size out of 5,9,13 or 19: "))

    state.screenHeight = int(input("Pick how large you want the game screen to be: "))
    state.set_n(n)

    state.mode = "Game"
    return state


def buttonFunctions(b,screen, state, pos):
    if b.function == "Pass":
        state.passCount += 1
        if state.player == "White":
            state.player = "Black"
        else:
            state.player = "White"
        if state.passCount == 3:
            gameMode = "End game."
                        



 
import pygame


pygame.init()
  
# Set the width and height of the screen [width,height]

state = setupGame()


size = [state.screenHeight+200,state.screenHeight]
screen = pygame.display.set_mode(size)

buttons =[]
text = [1,2]
buttons.append(button("Hello",(state.screenHeight,state.screenHeight/2),(100,50),(100,100,200),"Function"))
text.append(3)
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if onGrid(state.n,state.screenHeight, pos):
                state = rules.play(state, gridPosition(state.n,state.screenHeight,pos))
            for b in buttons:
                if b.isOn(pos):
                    buttonFunctions(b,screen, state, pos)
            
        if event.type == pygame.KEYDOWN:
            if state.textOut:
                textOut.printBoard(state.board.output(),4,state.n)
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  

  
    pos = pygame.mouse.get_pos()
    pos = snapMouse(state.n,state.screenHeight,pos)



    graphicalOut.draw(screen,state,pos,buttons)

    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(20)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

