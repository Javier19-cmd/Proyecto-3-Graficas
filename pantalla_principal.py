import random
from math import *

import pygame
from OpenGL.GL import *
from mapa1 import * 
from mapa3 import *

def main(): #Método para hacer una pantalla principal y un botón para iniciar el juego. 
    
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
    texto_faciles = fuente.render("Presiona el número 1 para los niveles fáciles.", 0, (0, 0, 0))
    texto_medios = fuente.render("Presiona el número 2 para los niveles medios.", 0, (0, 0, 0))


    #Haciendo estática la corrida.
    corrida = True
    while corrida:
        
        #Llenando la pantalla con el color de fondo.
        pantalla.fill(CELESTE)
        
        #Colocando el texto en la pantalla.
        #Niveles fáciles.
        pantalla.blit(texto_faciles, (100, 200))

        #Niveles medios.
        pantalla.blit(texto_medios, (100, 300))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                corrida = False
            #Si se presiona la tecla espacio, se inicia el juego.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                corrida = False
                cargar_mapa_facil() #Cargando mapas fáciles.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                corrida = False
                cargar_mapa_medio()

        pygame.display.flip() #Actualiza la pantalla.


def cargar_mapa_facil():

    pygame.init() #Inicializa pygame.
    screen = pygame.display.set_mode((800, 800)) #Crea la pantalla.
    r = Raycaster(screen) #Crea el raycaster.
    r.load_map("map.txt") #Carga el mapa.

    running = True
    while running: 
        screen.fill(BLACK, (0, 0, r.w, r.h)) #Limpia la pantalla.
        screen.fill(SKY, (r.w/500, 0, r.w, r.h/2)) #Llena el cielo.
        screen.fill(GROUND, (r.w/500, r.h/2, r.w, r.h/2)) #Llena el suelo.
        # x = random.randint(0, 500) #Genera un número aleatorio entre 0 y 500.
        # y = random.randint(0, 500) #Genera un número aleatorio entre 0 y 500.
        
        #r.pixel(x, y, WHITE) #Dibuja un punto blanco en la pantalla.
        #r.point(x, y) #Dibuja un pixel blanco en la pantalla.
        #r.block(x, y) #Dibuja un bloque blanco en la pantalla.
        r.clearZ()
        r.render() #Dibujando el mapa.
        pygame.display.flip() #Actualiza la pantalla.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d: #Si se presiona la tecla derecha.
                    # if r.player["a"] < 0:
                    #     r.player["x"] += 20
                    # else: 
                    #     r.player["x"] -= 20
                    r.player["a"] += pi/25

                    #r.collision(r.player["x"], r.player["y"])

                if event.key == pygame.K_a: #Si se presiona la tecla izquierda.
                    
                    # if r.player["a"] < 0:
                    #     r.player["x"] -= 20
                    #     print(r.player["a"])
                    # else:
                    #     r.player["x"] += 20
                    # print(r.player["a"])

                    r.player["a"] -= pi/25
                    r.collision(r.player["x"], r.player["y"])
                
                #Detectando si hay evento del mouse.
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1: #Si se presiona el botón izquierdo del mouse.
                     #Detectando el movimiento del mouse, para mover la cámara.
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_x = mouse_pos[0]
                        mouse_y = mouse_pos[1]

                        #Moviendo la cámara.
                        if mouse_x > 400:
                            r.player["a"] += pi/25
                        if mouse_x < 400:
                            r.player["a"] -= pi/25
            

                #Moverse en base a la dirección en la que se está mirando.
                if event.key == pygame.K_w: #Si se presiona la tecla arriba.
                    r.player["x"] += cos(r.player["a"]) * 50
                    r.player["y"] += sin(r.player["a"]) * 50
                    r.collision(r.player["x"], r.player["y"])
                if event.key == pygame.K_s: #Si se presiona la tecla abajo.
                    r.player["x"] -= cos(r.player["a"]) * 50
                    r.player["y"] -= sin(r.player["a"]) * 50
                    r.collision(r.player["x"], r.player["y"])

    
                # if event.key == pygame.K_a: #Si se presiona la tecla a.
                #     r.player["a"] -= pi/25
                
                # if event.key == pygame.K_d: #Si se presiona la tecla d.
                #     r.player["a"] += pi/25
            
                if event.key == pygame.K_ESCAPE: #Cerrar la ventana.
                    running = False

                # #Esto me lo inventé yo.
                # if event.key == pygame.K_w: #Si se presiona la tecla w.
                #     r.player["y"] += int(20 * sin(r.player["a"]))
                #     r.player["x"] += int(20 * cos(r.player["a"]))
                
                # if event.key == pygame.K_s: #Si se presiona la tecla s.
                #     r.player["y"] -= int(20 * sin(r.player["a"]))
                #     r.player["x"] -= int(20 * cos(r.player["a"]))


def cargar_mapa_medio(): #Cargando los niveles medios.
    
    pygame.init() #Inicializa pygame.
    screen2 = pygame.display.set_mode((800, 800)) #Crea la pantalla.
    r3 = Raycaster3(screen2) #Crea el raycaster.
    r3.load_map("map3.txt") #Carga el mapa.

    running = True
    while running: 
        screen2.fill(BLACK, (0, 0, r3.w, r3.h)) #Limpia la pantalla.
        screen2.fill(SKY, (r3.w/500, 0, r3.w, r3.h/2)) #Llena el cielo.
        screen2.fill(GROUND, (r3.w/500, r3.h/2, r3.w, r3.h/2)) #Llena el suelo.
        # x = random.randint(0, 500) #Genera un número aleatorio entre 0 y 500.
        # y = random.randint(0, 500) #Genera un número aleatorio entre 0 y 500.
        
        #r.pixel(x, y, WHITE) #Dibuja un punto blanco en la pantalla.
        #r.point(x, y) #Dibuja un pixel blanco en la pantalla.
        #r.block(x, y) #Dibuja un bloque blanco en la pantalla.
        r3.clearZ()
        r3.render() #Dibujando el mapa.
        pygame.display.flip() #Actualiza la pantalla.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d: #Si se presiona la tecla derecha.
                    # if r.player["a"] < 0:
                    #     r.player["x"] += 20
                    # else: 
                    #     r.player["x"] -= 20
                    r3.player["a"] += pi/25

                    #r.collision(r.player["x"], r.player["y"])

                if event.key == pygame.K_a: #Si se presiona la tecla izquierda.
                    
                    # if r.player["a"] < 0:
                    #     r.player["x"] -= 20
                    #     print(r.player["a"])
                    # else:
                    #     r.player["x"] += 20
                    # print(r.player["a"])

                    r3.player["a"] -= pi/25
                    r3.collision(r3.player["x"], r3.player["y"])
                
                #Detectando si hay evento del mouse.
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1: #Si se presiona el botón izquierdo del mouse.
                     #Detectando el movimiento del mouse, para mover la cámara.
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_x = mouse_pos[0]
                        mouse_y = mouse_pos[1]

                        #Moviendo la cámara.
                        if mouse_x > 400:
                            r3.player["a"] += pi/25
                        if mouse_x < 400:
                            r3.player["a"] -= pi/25
            

                #Moverse en base a la dirección en la que se está mirando.
                if event.key == pygame.K_w: #Si se presiona la tecla arriba.
                    r3.player["x"] += cos(r3.player["a"]) * 30
                    r3.player["y"] += sin(r3.player["a"]) * 30
                    r3.collision(r3.player["x"], r3.player["y"])
                if event.key == pygame.K_s: #Si se presiona la tecla abajo.
                    r3.player["x"] -= cos(r3.player["a"]) * 30
                    r3.player["y"] -= sin(r3.player["a"]) * 30
                    r3.collision(r3.player["x"], r3.player["y"])

    
                # if event.key == pygame.K_a: #Si se presiona la tecla a.
                #     r.player["a"] -= pi/25
                
                # if event.key == pygame.K_d: #Si se presiona la tecla d.
                #     r.player["a"] += pi/25
            
                if event.key == pygame.K_ESCAPE: #Cerrar la ventana.
                    running = False

                # #Esto me lo inventé yo.
                # if event.key == pygame.K_w: #Si se presiona la tecla w.
                #     r.player["y"] += int(20 * sin(r.player["a"]))
                #     r.player["x"] += int(20 * cos(r.player["a"]))
                
                # if event.key == pygame.K_s: #Si se presiona la tecla s.
                #     r.player["y"] -= int(20 * sin(r.player["a"]))
                #     r.player["x"] -= int(20 * cos(r.player["a"]))
main()