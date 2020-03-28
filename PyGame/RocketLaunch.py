#Main
import GlobalVariables as GetVar
import pygame
import GameLoop
import IntroLoop

#start the game
pygame.init()

#define the name of the game window
window = pygame.display.set_mode((GetVar.win_x, GetVar.win_y))

#give the game window a title
pygame.display.set_caption(GetVar.Title)

#game function
def RocketLaunch():
    
    #run the introloop
    IntroLoop.IntroLoop()

    #run the gameloop    
    GameLoop.GameLoop()
    
#run the game
RocketLaunch()

#end the game
pygame.quit()


