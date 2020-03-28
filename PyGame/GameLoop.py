import pygame
import GlobalVariables as GetVar
import GameDraw as Game
import SpriteCollection
import PauseLoop as Pause
    

#define the game loop
def GameLoop():
        
    #Game window
    window = pygame.display.set_mode((GetVar.win_x, GetVar.win_y))
    
    #clock
    clock = pygame.time.Clock()
    
    #loop
    while GetVar.GameState:
    
        #define the refresh rate
        #pygame.time.delay(GetVar.Refresh_Rate)
        clock.tick(60)
        
        #input processing
        keys = pygame.key.get_pressed()
    
        #allow the user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GetVar.GameState = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GetVar.PauseState = True
                    Pause.PauseLoop()
            

    
        if keys[pygame.K_LEFT] and GetVar.player_x_pos > 0:
            GetVar.player_x_pos -= GetVar.dx
            
        if keys[pygame.K_RIGHT] and GetVar.player_x_pos < GetVar.win_x - 25:
            GetVar.player_x_pos += GetVar.dx
        
        if keys[pygame.K_UP] and GetVar.player_y_pos > 0:
            GetVar.player_y_pos -= GetVar.dy
        
        if keys[pygame.K_DOWN] and GetVar.player_y_pos < GetVar.win_y - 25:
            GetVar.player_y_pos += GetVar.dy
    
        
        #draw the background
        Game.SolidBackgroundColor(window, "lightblue")
    
        #draw things to the screen
        Game.DrawSprite(window, SpriteCollection.GoldCoin, 45, 45,40 )
        Game.DrawSprite(window, SpriteCollection.PlayerRocket, GetVar.player_x_pos, GetVar.player_y_pos, 40)
    
        #update the display
        pygame.display.update()
    
    
    