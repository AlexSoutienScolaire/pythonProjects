# Pygame template - skeleton for a new pygame project

import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60

# Define colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Initialise pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# cacher le curseur

pygame.mouse.set_visible(0)

# curseur sprite

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,2))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
#        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT*0.9
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = mouse_pos[0]
        #self.rect.centery = mouse_pos[1]

# bille

class Bille(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = 425
        self.speedx = random.randrange(-5, 5)
        self.speedy = 10


        
        
    def update(self):
        
        if self.rect.x > WIDTH:
            self.speedx = -self.speedx
            
        if self.rect.x < 0:
            self.speedx = -self.speedx
            
        if self.rect.y > HEIGHT:
            self.speedy = -self.speedy
            
        if self.rect.y < 0:
            self.speedy = -self.speedy
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
    def inverser(self):
        self.speedx += random.randrange(-1,1)
        self.speedy = -self.speedy #+ random.randrange(-1,1)

class Brique(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y



all_sprites = pygame.sprite.Group()
billes = pygame.sprite.Group()
briques = pygame.sprite.Group()

cursor = Cursor()
all_sprites.add(cursor)



bille = Bille()
all_sprites.add(bille)
billes.add(bille)


for i in range(2,11):
    for j in range(2,11):
        b = Brique(i*30, j*30)
        all_sprites.add(b)
        briques.add(b)
        

# Game loop

running = True
while running:
    
    #keep loop running at the right speed 
    clock.tick(FPS)
    
    
    # Process input (events)
    for event in pygame.event.get():
        
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
            
    
    # check collision

    rebond = pygame.sprite.spritecollide(cursor, billes, False)
    if rebond :
        bille.inverser()
    
    # check collision with brique
    
    hits = pygame.sprite.groupcollide(billes, briques, False, True)
    # Update

    all_sprites.update()
            
    # Draw / Render

    screen.fill(BLACK)
    all_sprites.draw(screen)

    # AFTER drawing everything, flip the display
    
    pygame.display.flip()
    
pygame.quit()

