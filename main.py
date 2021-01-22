'''
Crear un termometro con pygame
>>El termometro tiene que aceptar entradas desde teclado de la temperatura



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

--Uno de los eventos es que podemos introducir datos directamente
    -Esto se hace en el control de eventos >> responderá solo ante las teclas numericas

--Control del selector para que cambie de F a C con hacer un solo click en cualquier lado de la pantalla y que tranforme el valor a F o a C respectivamente
    -un atributo: si va a estar en F o en C
    -un metodo: el cambio con el click (cambiando el disfraz)
    
---conversión > transformar lo que introducimos cuando hacemos click en el selector:
    -metedo convertir en Termometro()
    -luego en el def start, donde la revisión de eventos, hay que cambiar el selector para que deje de controlar el click
        >> porque ahora el click va a coectar tb el covnersor
'''


import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("termometro/termo1.png") # el disfraz
    
    def convertir(self, grados, toUnidad): #convertir grados C a F y viceversa
        resultado = 0 #variable donde guarda el resultado
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados-32)*5/9
        else: #si no es F ni C
            resultado = grados
            
        return '{:10.2f}'.format(resultado) #devuelve el resultado, de longitus 10 y con dos decimales
        
    
class Selector(): #este es el selector de Fº - Cº
    __tipoUnidad = None #esto es si es F o C
    
    def __init__(self, unidad='C'): #aqui estan los disfraces 
        self.__costumes1 = pygame.image.load('termometro/posiF.png') 
        self.__costumes2 = pygame.image.load('termometro/posiC.png')
        
        self.__tipoUnidad = unidad
        
    def custome(self): #es un getter, para que nos devuelva que disfraz a mostrar
        if self.__tipoUnidad == 'F':
            return self.__costumes1 #esta es la posición del disfraz para F
        else:
            return self.__costumes2
        
    def unidad(self): #esto es un getter para que devuelva F o C
        return self.__tipoUnidad
    
    def change (self): #este funciona como interruptor 
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
            

class NumberInput(): #este es el cuadrado donde se pone el valor del texto numerico que pongamos
    __valor = 0 # es el valor de cuadro en numerico, para las cuentas posteirore
    __strValue = "" # este es el atributo a renderizar, porque phyton pinta cadenas
    __position = [0,0] #un array con la posicion del cuadrado, con x e y
    __size = [0,0] #esto es para el tamaño del cuadrado, con ancho por alto
    __pointsCount = 0 #esto es para que cuente los puntos para los decimales
    
    def __init__(self, value = 0): #con valor por default 0
        self.__font = pygame.font.SysFont('Arial', 24) #esta es la fuente de las letras
        '''
       self. __strValue = str(value) # va con self. porque es n objeto de o trauto prinips
        try: # antes de hacer la asginación se hace un try,a dinganandolo
            self.__strValue = int(valor)
            self.__strValue = str(valor)
        except:
            psss
        '''
        self.value(value) #esto es lo mismo qqeu lo antrtior, pero menos farragmode

    def on_event(self, event): # esto es para que, si el unicode está en los valores puestos, l valor puesto hay que añadirlo al strValue para que lo imprima en pantalla 
        if event.type == KEYDOWN: #comprobar la tecla que se pulsa
            if event.unicode in '0123456789' and len(self.__strValue) < 10 or event.unicode == '.' and self.__pointsCount == 0:  #esto es para que compruebe si lo que pulsamos está dentro de ese conjunto de numeros y que se limite a un total de nueve digitos, 
       # if event.isdigit() >> otra forma de hacer lo anterior
                self.__strValue += event.unicode #así aparece el numero pulsado (solo el numero)                               
                self.value((self.__strValue)) # actualizar el value, para que quede el valor de lo que insertamos
                if event.unicode == '.':
                    self.__pointsCount += 1 # esto es para permitir introducir decimales con punto
            elif event.key == K_BACKSPACE: #comprbar si la tecla sea una determinada, en este caso la de borrar
                if self.__strValue[-1] == '.': #si la posicion penultima es igual a punto
                    self.__pointsCount -= 1 #para que si borramos el punto, podamos volver a colocar uno
                self.__strValue = self.__strValue[:-1] # esto es para que si pulsemos retroceso, solo vaya elimnando el ultimo digito -ya que coje desde el principio hasta el penultimo-
                self.value((self.__strValue))
         
        
        
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
    def value(self, val=None): # este es el getter del valor
        if val == None:
            return self.__value # este es el valor numerico
        else: #si se informa val
            val = str(val) #transformar el valor en una cadena
            try:
                self.__value = float(val) #esto es para comprobar que lo que metemos en un numero entero
                self.__strValue = val # en esta variable metemos la cadena
                if '.' in self.__strValue: #si strValue tiene punto >> cada vez que asignamos un valor, inicliazamos pointsCount ocn el valor adecuado 
                   self.__pointsCount = 1
                else:
                    self.pointsCount = 0
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
        
        self.selector = Selector() #esto sería para crear e iniciar el selector en main
        
        
    def __on_close(self): #sacamos la salida a esta funcion para acostumbrarnos a dejar las funciones pequeñas
        pygame.quit()
        sys.exit()


    def start(self):
        #control de eventos
        while True:
            for event in pygame.event.get(): #esto es para capturar los eventos y cerrar con la X
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event) # el va a comprobar si se han pulsado las teclas adecuadas y modificar su value
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change() #esto es el interruptor para que cambien el selector de tipo de unidad
                    grados = self.entrada.value() # este es para los grados que hemos introducido
                    nuevaUnidad = self.selector.unidad() #getter del tipo de unidad
                    temperatura = self.termometro.convertir(grados, nuevaUnidad) # esto llama al conersor
                    self.entrada.value(temperatura) #asignar el nuevo valor de la temperatura ya transformada al campo de entrada
            
            # Pintamos el fondo de pantalla
            self.__screen.fill((244,236,203)) #esto es repitar el fondo, para evitar que queden rastros de otros objetos
            
             #pintamos el termometro en su posicion
            self.__screen.blit(self.termometro.custome, (50,34)) #esto es para que pinte la imagen del termometro en esa posicion       
           
            #pintamos el cuadro de texto
            text = self.entrada.render() #obtenemos rectangulo con fondo blanco y foto de texto y la asignamos a la varaible text
            pygame.draw.rect(self.__screen, (255,255,255), text[0]) #esto es para que dibuje el recuadro con su posicion y tamaño, en la pantalla, que lo rellene de blanco y las cooredenada del fondo, (primera posicion)
            self.__screen.blit(text[1], self.entrada.pos()) #para pintar la foto del texto >> se usa custome porque es como un disfraz >> es la imagen del texto
            
            #pintamos el selector
            self.__screen.blit(self.selector.custome(), (112,153))
                               
                               
            pygame.display.flip() #refrescar la pantalla
                    

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()
    