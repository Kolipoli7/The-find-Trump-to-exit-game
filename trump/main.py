import pygame
import random
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Trump")


screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
trump_surf = pygame.image.load("trump/Trump.jpg").convert()
trump_rect = trump_surf.get_rect()

show_trump = False
font = pygame.font.Font(None,50)
text_surf = font.render("Search for Trump to exit", True, "white")
max_y = screen.get_height() - 400
max_x = screen.get_width() - 320


while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_t:
                show_trump = True
                trump_y = random.randint(0, max_y)
                trump_x = random.randint(0,max_x)
                trump_rect.topleft = (trump_x,trump_y)



        if event.type == pygame.MOUSEBUTTONDOWN:
            if trump_rect.collidepoint(event.pos):
                pygame.quit()
                exit()

            
        

    #draw
    if show_trump == True:
        screen.fill("black")
        screen.blit(trump_surf,trump_rect)

    screen.blit(text_surf,(500,10))
    
        
                
    

    pygame.display.update()
    clock.tick(60)

    


    