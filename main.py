'''
Crear un termometro con pygame

-class termómetro > la creamos por encima de mainApp porque tendremos que crear una instancia en mainApp posteriormente y asignarla a la variable termometro,
                    y python no la acepta si la creamos dentro del mainApp debajo de la variable que la llama (tiene que estar antes)
    -su init es el disfraz

-class number input > cuadrado donde aparece la temperatura:
    -recuadro blanco posicionado y otro recuadro dposicionado dentro para el texto
    -controlar los eventos de la pantalla para que cuando tecleamos texto lo situa en ese campo
    -solo acepte numeros
    >>Metodo: update(): cada vez que el ususrio teclee, va a comprobar lo que tecleemos y si es numero actualizara la pantalla
     -Gestionar las fuentes del texto >> la creamos __font   
        
        
-en mainApp metemos los tres atributos:
    -termometro
    -campo de entrada
    -selector de unidad
    
    >>metodo init
        -pantalla
        -titulo del programa
        -color de fondo
        -crear una instancia del objeto Termometro en vacio y se la asigno al atributo de la clase mainApp
        
    >>metodo close:
        aqui ponemos la salida
    >>metodo start -aqui meteremos todo-
        -bbucle infinito while true para poner el def close aqui y poder salir con la X
            >dentro tb va la imagen del termometro
            >poner otra vez el color del fondo de pantalla paa evitar que se qeuden copias o problemas si hay cambios de imagen
            + flip
            >pintar aqui tambien el recuadro del texto

'''


import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("termometro/termo1.png") # el disfraz
       
class NumberInput(): #este es el cuadrado donde se pone el valor del texto numerico que pongamos
    __valor = 0
    __strValue = '0' # este es el atributo a renderizar
    __position = [0,0] #un array con la posicion del cuadrado, con x e y
    __size = [0,0] #esto es para el tamaño del cuadrado, con ancho por alto
    
    def __init__(self, value = 0): #con valor por default 0
        self.__font = pygame.font.SysFont('Arial', 24) #esta es la fuente de las letras
        textBlock = self.__font.render(self._strValue, True, (74,74,74)) # variable que es bloque de texto renderizado, sin self porque solo es para aqui. (Se le pone la cadena a renderizar y el color)
        rect = textBlock.get_rect() #esto es la forma para obtener el rectangulo
        rect.left = self.__position[0]# a este rectangulo le informamos la posicion del lado izquierdo
        rect.top = self.__position[1] #esta es la posición del alto
        rect.size = self._size #aunque ya tenemos un recuadro con el tamaño del texto, ahora lo modificamos al que qeuramos
   
   #como position y size son privados de la otra clase, hay que crear setter y getters para informar aqui del tamaño del recuadro
    def value(self, val =None): # este es el getter del valor
        if val == None:
            return self.__value # este es el valor numerico
        else: #si se informa val
            val = str(val) #transformar el valor en una cadena
            try:
                self.__value = int(val) #esto es para comprobar que lo que metemos en un numero entero
                self.__strValue = val # en esta variable metemos la cadena
            except: # esto para si metemos algo que no es adecuado, va a pasar de el, no hacer nada
                pass
            
    def width(self, val=None): #setter del ancho del recuadro
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
    def height(self, val=None): #setter del alto del recuadro
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
        
    def size(self, val=None): 
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[0])
                self.__size = [int(val[0]),int(val[1])] # esto es para la comprobación
            except:
                pass
     
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption('Termómetro') #título del programa
        self.__screen.fill((244,236,203)) # esto es el color de fondo
        
        self.termometro = Termometro() #crear una instancia de termometro dentro de esa variable
        self.entrada = NumberInput() #esto es para crear el cuadrado donde ponemos el numero
        self.entrada.width(123)
        

        
        
    def __on_close(self): #sacamos la salida a esta funcion para acostumbrarnos a dejar las funciones pequeñas
        pygame.quit()
        sys.exit()


    def start(self):
        while True:
            for event in pygame.event.get(): #esto es para capturar los eventos y cerrar con la X
                if event.type == QUIT:
                    self.__on_close()
                    
            self.__screen.blit(self.termometro.custome, (50,34)) #esto es para que pinte la imagen del termometro en esa posicion       
            pygame.display.flip() #refrescar la pantalla
                    

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()
    