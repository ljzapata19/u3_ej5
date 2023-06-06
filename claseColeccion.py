from claseInterfaz import Interfaz

class Coleccion(Interfaz):
    __coleccion = list()
    def __init__(self):
        self.__coleccion = []
        
        
    def insertarElemento(self, elemento, posicion):
        try:
            if posicion < 0 or posicion > len(self.__coleccion):
                raise ValueError('Posicion no valida')
            self.__coleccion.insert(posicion, elemento)
            
        except ValueError:
            print('Debe ingresar un entero')
        
    
    def agregarElemento(self, elemento):
        self.__coleccion.append(elemento)
    
    def mostrarElemento(self, posicion):
        try:
            if posicion < 0 or posicion >= len(self.__coleccion):
                raise IndexError('Posicion no valida')
            print (self.__coleccion[posicion])
        except IndexError:
            print('Error al mostrar elemento.')
    