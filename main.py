from claseColeccion import Coleccion


def test():
    coleccion = Coleccion()
    coleccion.agregarElemento('Elemento 1')
    coleccion.agregarElemento('Elemento 2')
    coleccion.agregarElemento('Elemento 3')
    
    coleccion.mostrarElemento(1)
    coleccion.mostrarElemento(5)
    
    coleccion.insertarElemento('Elemento x', 0)
    coleccion.insertarElemento('Elemento y', 5)
    
    coleccion.mostrarElemento(0)
    coleccion.mostrarElemento(1)

if __name__ == '__main__':
    test()
    