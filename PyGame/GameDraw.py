#all the game drawing will be done here
import pygame
import Utilities as Utils


##################################################
def DrawRect(window_name, color_string, x, y, w, h):
        
    rgb = Utils.ColorString_to_RGB(color_string)
    dim = [x,y,w,h]
    pygame.draw.rect(window_name, rgb, dim)
    
##################################################
    
def SolidBackgroundColor(window_name, color_string):
    
    rgb = Utils.ColorString_to_RGB(color_string)
    window_name.fill(rgb)

##################################################
    
def Rect_Button(window_name, text_string, bg_color_string, font_color_string, font_style, font_size, x, y, w, h):
    
    #colors and position
    #font_rgb = Utils.ColorString_to_RGB(font_color_string)
    bg_rgb = Utils.ColorString_to_RGB(bg_color_string)
    button_dim = [x,y,w,h]
    
    #contents    
    pygame.draw.rect(window_name, bg_rgb, button_dim)
    
##################################################
    
def DrawSprite(window_name, file_path, x, y, scale):
    
    image = pygame.image.load(file_path)
    location = [x,y]
    #catch an error
    if scale == 0:
        scale = 1
    image = pygame.transform.scale(image, (scale,scale))
    #image = pygame.transform.scale(image, (image.get_rect()[0]*scale, image.get_rect()[1]*scale))
    window_name.blit(image, location)
    
##################################################
    
def DrawText(window_name, string, font, size, x, y, font_color):
    
    font = pygame.font.SysFont(font, size)
    text = font.render(string, True, Utils.ColorString_to_RGB(font_color), None)
    textRect = text.get_rect()
    textRect.center = (x,y)
    
    window_name.blit(text, textRect)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    