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
    -Una vez creado, hay que ponerlo en el refresco de imagen
        >>el probelma es como colocarlo con todas las variables que hemos creado (y algunos propias)
        --para solucionarlo creamos un metodo def render(self) y ponemos en el todas las varaibles con las poasiciones/tamaño
     - textBlock >> funciona como un disfraz >> es la imagen del texto 

-en mainApp metemos los tres atributos:
    -termometro
    -campo de entrada
    -selector de unidad
    
    >>def render():
        asegurar que el strValue (valor de entrada) sea el adecuado y no acepte letras
        para eso hay que inicializarlo en el init
    
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
    __valor = 0 # es el valor de cuadro en numerico, para las cuentas posteirore
    __strValue = '0' # este es el atributo a renderizar, porque phyton pinta cadenas
    __position = [0,0] #un array con la posicion del cuadrado, con x e y
    __size = [0,0] #esto es para el tamaño del cuadrado, con ancho por alto
    
    def __init__(self, value = 0): #con valor por default 0
        self.__font = pygame.font.SysFont('Arial', 24) #esta es la fuente de las letras
        self. __strValue = str(value) # va con self. porque es n objeto de o trauto prinips
        
    def render(self): #metodo con todo lo relacionado de renderización
        textBlock = self.__font.render(self.__strValue, True, (74,74,74)) # variable que es bloque de texto renderizado, sin self porque solo es para aqui. (Se le pone la cadena a renderizar y el color) >> genera el recuadro con el numero
        rect = textBlock.get_rect() #esto es la forma para obtener el rectangulo
        rect.left = self.__position[0]# a este rectangulo le informamos la posicion del lado izquierdo
        rect.top = self.__position[1] #esta es la posición del alto
        rect.size = self.__size #aunque ya tenemos un recuadro con el tamaño del texto, ahora lo modificamos al que qeuramos
        #hay que devolver lo que necesitamos para pintarlo > texto y el recuadro grande blanco >> como hay que devolver dos variables, lo hacemos con diccionario o una tupla
            #con una tupla >> accederíamos al fondo usando [0] y al texto con [1]
        return (rect,textBlock)
    
        '''
            con dicconario
        return {
            'fondo': rect,
            'texto': textBlock
            }
        '''        
        
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
                
                
    def posX(self, val=None): #setter de la position X del recuadro
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def posY(self, val=None): #setter del alto del recuadro
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
        
    def pos(self, val=None): 
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]),int(val[1])]
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
        self.entrada.pos((106,58)) # esta es la posicion de nuestro recuadro de texto
        self.entrada.size((133,28))
        
        
    def __on_close(self): #sacamos la salida a esta funcion para acostumbrarnos a dejar las funciones pequeñas
        pygame.quit()
        sys.exit()


    def start(self):
        while True:
            for event in pygame.event.get(): #esto es para capturar los eventos y cerrar con la X
                if event.type == QUIT:
                    self.__on_close()
             
             #pintamos el termometro en su posicion
            self.__screen.blit(self.termometro.custome, (50,34)) #esto es para que pinte la imagen del termometro en esa posicion       
           
            #pintamos el cuadro de texto
            text = self.entrada.render() #obtenemos rectangulo con fondo blanco y foto de texto y la asignamos a la varaible text
            pygame.draw.rect(self.__screen, (255,255,255), text[0]) #esto es para que dibuje el recuadro con su posicion y tamaño, en la pantalla, que lo rellene de blanco y las cooredenada del fondo, (primera posicion)
            self.__screen.blit(text[1], self.entrada.pos()) #para pintar la foto del texto >> se usa custome porque es como un disfraz >> es la imagen del texto
            
            pygame.display.flip() #refrescar la pantalla
                    

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()
    