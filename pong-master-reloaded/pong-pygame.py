# -*- coding: utf-8 -*-

import pygame

#Colores
BLANCO =  (255, 255, 255)
NEGRO = (0, 0, 0)

pygame.init()

dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("El pong de Programá tu Futuro Reloaded")
imagen_protagonista = pygame.image.load("image.png").convert()
imagen2_protagonista = pygame.image.load("image2.png").convert()
imagen_protagonista.set_colorkey(NEGRO)
imagen2_protagonista.set_colorkey(NEGRO)
pulsar_sonido = pygame.mixer.Sound("qubodup-cfork-ccby3-jump.ogg")
# Posición de partida del protagonista
rect_x = 325
rect_y = 50

# Velocidad y dirección del protagonista
rect_cambio_x = 5
rect_cambio_y = 5

# Velocidad en píxeles por fotograma
x_speed = 0
y_speed = 0
 
# Posición del bloque
x_coord = 500
y_coord = 450

hecho = False
arrancar = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            arrancar=True
            if evento.key == pygame.K_LEFT:
                x_speed = -3
            if evento.key == pygame.K_RIGHT:
                x_speed = 3
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            if evento.key == pygame.K_RIGHT:
                x_speed = 0
    
    pantalla.fill(NEGRO)        
    #Dibujamos el rectangulo y protagonista
    pygame.draw.rect(pantalla,BLANCO,[x_coord, y_coord, 160,20])
    pantalla.blit(imagen2_protagonista, [rect_x,rect_y])
    # Mueve el punto de partida de la bol al presionar una tecla
    if arrancar:
        rect_x += rect_cambio_x
        rect_y += rect_cambio_y
        x_coord += x_speed
        y_coord += y_speed
    
    # Cambia imagen cuando el personaje viene cayendo
    if rect_cambio_y < 0 :
        pantalla.fill(NEGRO)
        pantalla.blit(imagen_protagonista, [rect_x,rect_y])
        pygame.draw.rect(pantalla,BLANCO,[x_coord, y_coord, 160,20])
    
    # Rebota contra los bordes y el bloque
    if rect_y == 410:
        if rect_x > x_coord and rect_x <(x_coord + 160):
            rect_cambio_y = rect_cambio_y * -1
            pulsar_sonido.play()
            
    if rect_x > 650 or rect_x < 0:          
        rect_cambio_x = rect_cambio_x * -1   
        
    if rect_y < 0:          
        rect_cambio_y = rect_cambio_y * -1
    
    # Se detine cuando cae 
    if rect_y > 460:
        rect_cambio_y = rect_cambio_x = 0
              
        
    pygame.display.flip()
    reloj.tick(60)
    
pygame.quit()
