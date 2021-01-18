'''
Crear un termometro con pygame

-en mainApp metemos los tres atributos:
    -termometro
    -campo de entrada
    -selector de unidad
    
    >>modulo init
        -pantalla
        -titulo del programa
        -color de fondo
        
    >>modulo close:
        aqui ponemos la salida
    >>modulo start -aqui meteremos todo-
        -bbucle infinito while true para poner el def close aqui y poder salir con la X
'''


import pygame, sys
from pygame.locals import *

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption('Termómetro') #título del programa
        self.__screen.fill((244,236,203)) # esto es el color de fondo
        
    def __on_close(self): #sacamos la salida a esta funcion para acostumbrarnos a dejar las funciones pequeñas
        pygame.quit()
        sys.exit()


    def start(self):
        while True:
            for event in pygame.event.get(): #esto es para capturar los eventos y cerrar con la X
                if event.type == QUIT:
                    self.__on_close()
                    
            pygame.display.flip() #refrescar la pantalla
                    

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()
    