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
planet=pygame.transform.scale(pygame.image.load("jupiter.png"),(planet_size*2,planet_size*2))

white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)

class spaceCraft:
    def __init__(self,x,y,velx,vely,mass):
        self.x=x
        self.y=y
        self.velx=velx
        self.vely=vely
        self.mass=mass

    def move(self,planet=None):
        self.x += self.velx
        self.y +=self.vely
    
    def draw(self):
        pygame.draw.circle(screen,red,(int(self.x),int(self.y)),obj_size)

class Planet:
    def __init__(self,x,y,mass):
        self.x=x
        self.y=y
        self.mass=mass

    def draw(self):
        screen.blit(planet,(self.x-planet_size,self.y-planet_size))

def createObj(loc,mouse):
    tx,ty=loc
    mx,my=mouse
    velx=(mx-tx)/vel_scale
    vely=(my-ty)/vel_scale
    obj=spaceCraft(tx,ty,velx,vely,ship_mass)
    return obj

def main():
    running = True
    clock=pygame.time.Clock()

    Object=[]
    temp_obj_pos=None
    planet=Planet(width//2,height//2,planet_mass)

    while running:
        clock.tick(fps)

        mouse_pos=pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type== pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    
                    object=createObj(temp_obj_pos,mouse_pos)
                    Object.append(object)
                    temp_obj_pos=None
                else:
                    temp_obj_pos=mouse_pos

        screen.blit(bg,(0,0))
        
        if temp_obj_pos:
            pygame.draw.line(screen,white,temp_obj_pos,mouse_pos)
            pygame.draw.circle(screen,red,temp_obj_pos,obj_size)
            
        for object in Object[:]:
            object.draw()
            object.move()

            offscreen=object.x<0 or object.y<0 or object.x>width or object.y>height
            collided=math.sqrt((object.x-planet.x)**2 + (object.y-planet.y)**2)<=planet_size
            if offscreen or collided:
                Object.remove(object)
        
        planet.draw()
        pygame.display.update()
    
    pygame.quit()

if __name__=="__main__":
    main()