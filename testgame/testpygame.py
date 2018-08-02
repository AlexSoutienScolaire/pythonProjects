import pygame, sys
from pygame.locals import *

pygame.init()

couleur_fond = (255,255,0)

rouge = (255,0,0)
vert = (0,255,0)
bleu = (0,0,255)

couleur_cercle = rouge
rayon_cercle = 10
largeur =800
hauteur =600


resolution_ecran = (largeur, hauteur)

ecran = pygame.display.set_mode(resolution_ecran)

TDR = 50
horlogeTDR = pygame.time.Clock()

sourisX = 0
sourisY = 0



def tracerCercle(X, Y):
    return pygame.draw.circle(ecran, couleur_cercle, (X,Y), rayon_cercle)

ecran.fill(couleur_fond)  


while True:
    
    

    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEMOTION :
            sourisX, sourisY = event.pos
            est_clicke = event.buttons[0]
            if est_clicke ==1:
                tracerCercle(sourisX, sourisY)
               
        if event.type == KEYDOWN and event.key == K_a:
            couleur_cercle = rouge
            
        if event.type == KEYDOWN and event.key == K_b:
            couleur_cercle = vert

        if event.type == KEYDOWN and event.key == K_c:
            couleur_cercle = bleu

            
        if event.type == KEYDOWN and event.key ==  K_SPACE:
            ecran.fill(couleur_fond)
    #pygame.draw.circle(ecran, couleur_cercle, (sourisX, sourisY), rayon_cercle)
    horlogeTDR.tick(TDR)
    pygame.display.update()
