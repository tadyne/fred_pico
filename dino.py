import pygame
import sys
from pygame.locals import *
pygame.init()


surface = pygame.display.set_mode((700,500))    #setup okna
pygame.display.set_caption("dinosaurus")        #název okna
img = pygame.image.load("dino game/.venv/Fred1.png")       #načítam Freda
pygame.display.set_icon(img)                    #dávam freda jako ikonu


imp = pygame.image.load("dino game/.venv/background.png").convert()    #dávám pozadí


ground_img = pygame.image.load('dino game/.venv/ground,2.png')   
 
# Using blit to copy content from one surface to other
surface.blit(imp, (0, 0))

font = pygame.font.Font(None, 30)#styl a velikost písma
clock = pygame.time.Clock()#přidává čas

ground_scroll = 0
scroll_speed = 4            #rychlost dinosaura


#poloha objektu
x = 210
y = 310


#velikost objektu
width = 20
height = 20

vel = 10 #rychlost pohybu


#síla a vaha
v = 10
m = 1




class Fred(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f"dino game/.venv/Fred{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        DEFAULT_IMAGE_SIZE = (80, 80)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect = [x, y]

    def update(self): 
        self.counter += 1
        run_cooldown = 5

        if self.counter > run_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

Fred_group = pygame.sprite.Group()

dino = Fred(200, 300)

Fred_group.add(dino)


running = True
isjump = False          #funkce skoku neni aktivní

while running:          #základní loop

    fps = 50
    clock.tick(fps)      #udává Fps
     
    #vypnutí pomocí x
    for event in pygame.event.get(): 
   
        if event.type == pygame.QUIT: 
 
            running = False


    # základní pohyby dinosaura 
    keys = pygame.key.get_pressed() 
        
    if isjump == False: 

        if keys[pygame.K_UP]: 
 
            isjump = True
               
    if isjump : 
        # výpočet síly a rychlosti 
        F =(1 / 2)*m*(v**2) 
        y-= F 
        v = v-1
        if v<0: 
            m =-1

        if v ==-11:   
            isjump = False

            v = 10
            m = 1
    
    #zobrazuji pozadí
    surface.blit(imp, (0, 0)) 


    Fred_group.draw(surface)
    Fred_group.update()






    #načítám a zobrazuji freda
    din = pygame.image.load("dino game/.venv/Fred1.png").convert_alpha()
    DEFAULT_IMAGE_SIZE = (90, 90)
    din = pygame.transform.scale(din, DEFAULT_IMAGE_SIZE)
    surface.blit(din, (x, y, width, height))    


    pygame.draw.line(surface, (0, 0, 0), #vytvařime podlahu
                 [000, 400], 
                 [700, 400], 3)
    

    # vytvářím text fps
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0,0,0))
    surface.blit(fps_text, (10, 10))
    

    score_text = font.render(f"Skóre: {int(pygame.time.get_ticks() / 100)}", True, (0,0,0))
    surface.blit(score_text, (570, 10))



    Skore = int(pygame.time.get_ticks() / 100)
    if Skore >= 100:
        scroll_speed = 8





    # posun podlahy
    surface.blit(ground_img, (ground_scroll, 400))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0



    pygame.display.update()
      

 
  
# closes the pygame window  
pygame.quit()
sys.exit()
         

