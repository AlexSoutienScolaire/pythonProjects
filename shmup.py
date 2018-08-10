# Pygame template - skeleton for a new pygame project

import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# Define colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)






# Initialise pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SCHMUP")
clock = pygame.time.Clock()

# Player sprite

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        
        # get pressed key at each update
        keystate = pygame.key.get_pressed()
        
        # react to pressed key 
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
            
        if keystate[pygame.K_UP]:
            self.speedy = -5
            
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        
        # constraint player into the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH          
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.top < 0:
            self.rect.top = 0
            
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            
                
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.speedy)
        all_sprites.add(bullet)
        bullets.add(bullet)

# MOB Classe

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT +10 or self.rect.left < -25 or self.rect.right > WIDTH +20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5 )
        
# Bullet class
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, z):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 + z
        
    def update(self):
        self.rect.y += self.speedy
        
        #kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill
        
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)



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
        
        elif event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_SPACE:
                player.shoot()
    # Update
    all_sprites.update()
    
    #check to see if a bullet hits a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    
    for hit in hits : 
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    
    # check to see if a mob hit a player
    
    hits = pygame.sprite.spritecollide(player, mobs, False)
    
    if hits:
        running = False
            
            
    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # AFTER drawing everything, flip the display
    pygame.display.flip()
    
pygame.quit()

