class Pila:
    def __init__(self):
        self.valores = []

    #Funcion para agregar elementos a la pila
    def apilar(self,valor):
        self.valores.insert(0,valor)
    
    #Funcion para verificar si la pila esta vacia
    def pilaVacia(self):
        if(len(self.valores) == 0):
            return True
        else:
            return False
    
    #Funcion para quitar elementos de la pila
    def desapilar(self):
        if(self.pilaVacia()):
            return False
        else:
            self.valores.pop(0)
    
    #Funcion para vaciar la pila
    def vaciarPila(self):
        if(self.pilaVacia()):
            return False
        else:
            for i in range(len(self.valores)):
                self.desapilar()
            
            return True
    
    #Funcion para calcular el promedio
    def promedio(self):
        total = 0

        for i in self.valores:
            total += i
    
        return total/len(self.valores)

    #Funcion para obtener la pila
    def getPila(self):
        return self.valores

    #Funcion para contar consonantes
    def ContarConsonantes(self):
        cant = 0
        for a  in self.valores:
            if a not in ['a','e','i','o','u']:
                cant += 1
    
        return cant

    #Funcion para contar vocales
    def ContarVocales(self):
        cant = 0
        for a  in self.valores:
            if a in ['a','e','i','o','u']:
                cant += 1
    
        return cant

