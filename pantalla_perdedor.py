import random
from math import *

import pygame
from OpenGL.GL import *

def pantalla_perdedor():
    pygame.init()

    #Propiedades de la pantalla principal.

    #Definiendo el color celeste.
    CELESTE = (178, 255, 255)
    
    #Tamaño de la pantalla.
    pantalla = pygame.display.set_mode((800, 800))

    #Título de la pantalla.
    pygame.display.set_caption("Proyecto 3 - Raycasting")

    #Texto de la pantalla principal.
    fuente = pygame.font.SysFont("Arial", 30)
    texto = fuente.render("¡Perdiste!", 0, (0, 0, 0))

    #Haciendo estática la corrida.
    corrida = True
    while corrida:
        
        #Llenando la pantalla con el color de fondo.
        pantalla.fill(CELESTE)
        
        #Colocando el texto en la pantalla.
        pantalla.blit(texto, (350, 400))

        #Detectando eventos.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                corrida = False

        pygame.display.flip() #Actualiza la pantalla.

#pantalla_perdedor()