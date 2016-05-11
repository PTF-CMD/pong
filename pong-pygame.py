# -*- coding: utf-8 -*-

import pygame

#Colores
BLANCO =  (255, 255, 255)
NEGRO = (0, 0, 0)

pygame.init()

dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("El pong de Programá tu Futuro")

# Posición de partida de la bola
rect_x = 325
rect_y = 50

# Velocidad y dirección de la bola
rect_cambio_x = 5
rect_cambio_y = 5

# Velocidad en píxeles por fotograma
x_speed = 0
y_speed = 0
 
# Posición actual
x_coord = 10
y_coord = 450

fuente=pygame.font.Font(None, 25)
texto = fuente.render("CMD", True, NEGRO)
texto2 = fuente.render("Trabajo en Equipo", True, NEGRO)

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
    #Dibujamos el rectangulo, la bola y las letras
    pygame.draw.rect(pantalla,BLANCO,[x_coord, y_coord, 160,20])
    pygame.draw.ellipse(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
    pantalla.blit(texto, [rect_x + 5, rect_y + 10])
    pantalla.blit(texto2, [x_coord + 1, y_coord])
    # Mueve el punto de partida de la bol al presionar una tecla
    if arrancar:
        rect_x += rect_cambio_x
        rect_y += rect_cambio_y
        x_coord += x_speed
        y_coord += y_speed
        
    # Rebota contra los bordes.
    if rect_x >= x_coord and rect_x <= (x_coord + 160):
        if rect_y == 410: 
            rect_cambio_y = rect_cambio_y * -1
    
    if rect_x > 650 or rect_x < 0:          # Si el valor de x es mayor a 650 y menor a 0 píxeles,
        rect_cambio_x = rect_cambio_x * -1  # modifico la tasa de cambio, de positiva, a negativa. 
    if rect_y > 450 or rect_y < 0:          # Si el valor de y es mayor a 450 y menor a 0 píxeles,
        rect_cambio_y = rect_cambio_y * -1  # modifico la tasa de cambio, de pos
    
            
    pygame.display.flip()
    reloj.tick(60)
    
pygame.quit()
