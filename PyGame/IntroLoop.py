import GlobalVariables as GetVar
import pygame
import GameDraw as Game
import SpriteCollection

#define the title menu loop
def IntroLoop():
    
    #game window
    window = pygame.display.set_mode((GetVar.win_x, GetVar.win_y))
    
    #intro loop
    while GetVar.IntroState:
            
        #define the refresh rate
        pygame.time.delay(GetVar.Refresh_Rate)
    
        #allow the user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GetVar.IntroState = False
                GetVar.GameState = False
                        
        #draw the intro screen art
        Game.DrawSprite(window, SpriteCollection.IntroArt, 0, 0, 500)
                
        #set the background color
       # Game.SolidBackgroundColor(window, "ghostwhite")
        
        #some other stuff here
        Game.Rect_Button(window, "", "limegreen", "", "", 0, GetVar.win_x*0.25, GetVar.win_y*0.75, 50, 25)
        Game.Rect_Button(window, "", "red", "", "", 0, GetVar.win_x*0.65, GetVar.win_y*0.75, 50, 25)
        
        #Draw some text for the buttons
        Game.DrawText(window, "Start", 'Impact', 23, GetVar.win_x*0.299, GetVar.win_y*0.772, "black")
        Game.DrawText(window, "Exit", 'Impact', 24, GetVar.win_x*0.699, GetVar.win_y*0.775, "black")
        
        #see if the mouse is hovering over the button 
        MousePos = pygame.mouse.get_pos()
       
        if MousePos[0] > GetVar.win_x*0.25 and MousePos[0] < GetVar.win_x*0.25 + 50:
            if MousePos[1] > GetVar.win_y*0.75 and MousePos[1] < GetVar.win_y*0.75 + 25:
                Game.Rect_Button(window, "", "lime", "", "", 0, GetVar.win_x*0.25, GetVar.win_y*0.75, 50, 25)
                if pygame.mouse.get_pressed()[0]:
                    GetVar.IntroState = False
                
        if MousePos[0] > GetVar.win_x*0.65 and MousePos[0] < GetVar.win_x*0.65 + 50:
            if MousePos[1] > GetVar.win_y*0.75 and MousePos[1] < GetVar.win_y*0.75 + 25:
                Game.Rect_Button(window, "", "lightcoral", "", "", 0, GetVar.win_x*0.65, GetVar.win_y*0.75, 50, 25)
                if pygame.mouse.get_pressed()[0]:
                   pygame.quit()
        
                
        #update the display
        pygame.display.update()
    
    
