# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:53:54 2018

@author: AlexSoutienSco
"""

import pygame, sys

from pygame.locals import *

largeur = 1000
hauteur = 800

resolution = (largeur, hauteur)

surface_du_jeu = pygame.display.set_mode(resolution)
autre_surface = pygame.Surface(surface_du_jeu.get_size())

FPS = 25
fpsClock = pygame.time.Clock()

noir=(0,0,0)
blanc = (255,255,255)
vert = (0, 255, 0)
bleu = (0,0,255)
rouge = (255,0,0)

sourisX = 0
sourisY = 0
taille = 5

couleur_stylo = bleu
start_pos = (0,0)

autre_surface.fill(blanc)

while True:

    surface_du_jeu.fill(blanc)

    for event in pygame.event.get():
        
        if event.type == QUIT or event.type==KEYUP and event.key==K_ESCAPE:
            pygame.quit()
            sys.exit()            
            
        if event.type == MOUSEMOTION :
            end_pos = event.pos
            if event.buttons[0]==1:
                pygame.draw.line(autre_surface, couleur_stylo, start_pos, end_pos, taille)
            start_pos = end_pos
    
        if pygame.key.get_pressed()[K_a]:
            couleur_stylo = rouge
            
        if pygame.key.get_pressed()[K_z]:
            couleur_stylo = bleu
            
        if pygame.key.get_pressed()[K_e]:
            couleur_stylo = vert
            
        if pygame.key.get_pressed()[K_b]:
            taille +=1
            
        if pygame.key.get_pressed()[K_n]:
            if taille>2:
                taille-=1
            
        if pygame.key.get_pressed()[K_SPACE]:
            autre_surface.fill(blanc)
  
    surface_du_jeu.blit(autre_surface, (0,0))
    
    sourisX, sourisY = pygame.mouse.get_pos()
    pygame.draw.circle(surface_du_jeu, noir, (sourisX, sourisY), taille+2,int((taille+2)/5)+1)
    pygame.draw.circle(surface_du_jeu, couleur_stylo, (sourisX, sourisY) , taille)
   
    pygame.display.update()
    fpsClock.tick(FPS)
        