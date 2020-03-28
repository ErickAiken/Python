import GlobalVariables as GetVar
import pygame
import GameDraw as Game


def PauseLoop():
    
    #game window
    window = pygame.display.set_mode((GetVar.win_x, GetVar.win_y))
    
    #intro loop
    while GetVar.PauseState:
            
        #define the refresh rate
        pygame.time.delay(GetVar.Refresh_Rate)
    
        #allow the user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GetVar.PauseState = False
                GetVar.GameState = False
                        
        #set the background color
        Game.SolidBackgroundColor(window, "pink")
        
        #some other stuff here
        Game.Rect_Button(window, "", "limegreen", "", "", 0, GetVar.win_x*0.25, GetVar.win_y*0.75, 50, 25)
        Game.Rect_Button(window, "", "red", "", "", 0, GetVar.win_x*0.65, GetVar.win_y*0.75, 50, 25)
        
        #see if the mouse is hovering over the button 
        MousePos = pygame.mouse.get_pos()
        if MousePos[0] > GetVar.win_x*0.25 and MousePos[0] < GetVar.win_x*0.25 + 50:
            if MousePos[1] > GetVar.win_y*0.75 and MousePos[1] < GetVar.win_y*0.75 + 25:
                Game.Rect_Button(window, "", "lime", "", "", 0, GetVar.win_x*0.25, GetVar.win_y*0.75, 50, 25)
                LeftClick = pygame.mouse.get_pressed()[0]
                if LeftClick == True:
                    GetVar.PauseState = False
                
        if MousePos[0] > GetVar.win_x*0.65 and MousePos[0] < GetVar.win_x*0.65 + 50:
            if MousePos[1] > GetVar.win_y*0.75 and MousePos[1] < GetVar.win_y*0.75 + 25:
                Game.Rect_Button(window, "", "lightcoral", "", "", 0, GetVar.win_x*0.65, GetVar.win_y*0.75, 50, 25)
                
        
                
        #update the display
        pygame.display.update()