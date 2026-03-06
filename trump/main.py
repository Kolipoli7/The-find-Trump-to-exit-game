import pygame
import random
from sys import exit
import os
import sys

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Trump")
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
trump_surf = pygame.image.load(resource_path("trump/Trump.jpg")).convert()
trump_rect = trump_surf.get_rect()

show_trump = False
font = pygame.font.Font(None,50)
font2 = pygame.font.Font(None,40)
text_surf = font.render("Search for Trump to exit", True, "white")
text_surf2 = font2.render("Nonono", True, "white")
text_surf3 = font2.render("Find my friend first", True , "white")
epstein = pygame.image.load(resource_path("trump/epstein_nobg.png")).convert_alpha()
epstein_rect = epstein.get_rect()
epstein_rect.midleft = (0,500)
max_y = screen.get_height() - 400
max_x = screen.get_width() - 320
show_epstein = False


while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_t:
                show_trump = True
                trump_y = random.randint(0, max_y)
                trump_x = random.randint(0,max_x)
                trump_rect.topleft = (trump_x,trump_y)

        if event.type == pygame.QUIT:
            show_epstein = True




        if event.type == pygame.MOUSEBUTTONDOWN:
            if trump_rect.collidepoint(event.pos):
                pygame.quit()
                exit()


    #draw
    screen.fill("black")
    if show_trump == True:
        
        screen.blit(trump_surf,trump_rect)

    if show_epstein == True:
        screen.blit(epstein, epstein_rect)
        screen.blit(text_surf2,(200,400))
        screen.blit(text_surf3,(200,450))
        

    screen.blit(text_surf,(500,10))
    
            
    
        
                
    

    pygame.display.update()
    clock.tick(60)
    if show_epstein == True:
        pygame.time.delay(3000)
        show_epstein = False
    


    