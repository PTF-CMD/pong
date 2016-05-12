import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 450))
pygame.display.set_caption('Hello World!')
while True: # main game loop
	for event in pygame.event.get():
		#print(pygame.event.get())
		if event.type == KEYDOWN:
			#print "keydown"
			#print event
			if event.scancode == 111 or event.scancode == 25:
				print "arriba"
				while pygame.event.get() == []:
					print "nada"
				print "keyup arriba"
				print (pygame.event.get())

			elif event.scancode == 113 or event.scancode == 38:
				print "izquierda"
				while pygame.event.get() == []:
					print "nada"
				print "keyup izquierda"
				print (pygame.event.get())

			elif event.scancode == 116 or event.scancode == 39:
				print "abajo"
				while pygame.event.get() == []:
					print "nada"
				print "keyup abajo"
				print (pygame.event.get())

			elif event.scancode == 114 or event.scancode == 40:
				print "derecha"
				while pygame.event.get() == []:
					print "nada"
				print "keyup derecha"
				print (pygame.event.get())

		elif event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

#	for event in pygame.event.get():
#					print("hola")
#					if event.type == KEYUP:
#						print "keyup"
#						while event.scancode != 111 and event.scancode != 25:
#							print "termino arriba"