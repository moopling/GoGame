black    = (   0,   0,   0)
background = (255,219,112)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue = (0,0,255)

def drawBoard(n,screen,screenHeight):
  delta = screenHeight/n
	for i in range(n):
		pygame.draw.line(screen, (0,0,0),[(i+0.5)*delta,0.5*delta],[(i+0.5)*delta,(n-0.5)*delta])
		pygame.draw.line(screen, (0,0,0),[0.5*delta,(i+0.5)*delta],[(n-0.5)*delta,(i+0.5)*delta])


def drawStones(n,screen,screenHeight,board):
        stones = board.output()
        delta = screenHeight/n
        for x in range(n):
            for y in range(n):
                    if stones[x][y] == "Black":
                            pygame.draw.circle(screen,black,(int((x+0.5)*delta),int((y+0.5)*delta)),int(delta*0.4))
                    if stones[x][y] == "White":
                            pygame.draw.circle(screen,white,(int((x+0.5)*delta),int((y+0.5)*delta)),int(delta*0.4))
                  
	
import pygame
def draw(screen,state,pos,buttons):
        
 



  
        screen.fill(background)


        drawBoard(state.n,screen,state.screenHeight)
        drawStones(state.n,screen,state.screenHeight,state.board)

        for b in buttons:
                pygame.draw.rect(screen,b.colour,[b.pos[0],b.pos[1],b.size[0],b.size[1]])
   
    
        if state.player == "Black":
                colour = black
        else: colour = white
    
        pygame.draw.circle(screen,colour,pos,5)



    
        # Select the font to use. Default font, 25 pt size.
        font = pygame.font.Font(None, 25)
 

        strPlayer = "Player: " + state.player
        strCapdB = "White: " + str(state.captured["Black"])
        strCapdW = "Black: " + str(state.captured["White"])
        

        renderedText = font.render(strPlayer,True,black)
        screen.blit(renderedText, [state.screenHeight+25,0])

        renderedText = font.render(strCapdB,True,black)
        screen.blit(renderedText, [state.screenHeight+25,30])

        renderedText = font.render(strCapdW,True,black)
        screen.blit(renderedText, [state.screenHeight+25,60])

        for b in buttons:
                renderedText = font.render(b.text,True,black)
                screen.blit(renderedText, [b.pos[0]+5,b.pos[1]+int(0.5*b.size[1])-13])

