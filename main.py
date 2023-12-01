import pygame
import math

# pygame setup
pygame.init()

width,height=800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravitational slingshot effect")

planet_mass=100
ship_mass=5
g=5
fps=60
planet_size=50
obj_size=5
vel_scale=100

bg=pygame.transform.scale(pygame.image.load("background.jpg"),(width,height))
planet=pygame.transform.scale(pygame.image.load("background.jpg"),(planet_size*2,planet_size*2))

white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)

def main():
    running = True
    clock=pygame.time.Clock()

    Object=[]
    temp_obj_pos=None


    while running:
        clock.tick(fps)

        mouse_pos=pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type== pygame.MOUSEBUTTONDOWN:
                temp_obj_pos=mouse_pos

        screen.blit(bg,(0,0))
        if temp_obj_pos:
            pygame.draw.line(screen,white,temp_obj_pos,mouse_pos)
            pygame.draw.circle(screen,red,temp_obj_pos,obj_size)
            

        
        pygame.display.update()
    
    pygame.quit()

if __name__=="__main__":
    main()