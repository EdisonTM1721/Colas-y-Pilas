class Cola:
    def __init__(self):
        self.valores = []

    #Funcion para agregar elementos a la cola
    def encolar(self,valor):
        self.valores.append(valor)

    #Funcion para verificar si la cola esta vacia
    def colaVacia(self):
        if(len(self.valores) == 0):
            return True
        else:
            return False

    #Funcion para quitar elementos de la cola
    def desencolar(self):
        if(self.colaVacia()):
            return False
        else:
            self.valores.pop(0)
            return True

    #Funcion para obtener la cola
    def getCola(self):
        return self.valores

    #Funcion para vaciar la cola
    def vaciarCola(self):
        if(self.colaVacia()):
            return False
        else:
            for i in range(len(self.valores)):
                self.desencolar()
            return True
            
    #Funcion para obtener el promedio
    def promedio(self):
        total = 0

        for i in self.valores:
            total += i
    
        return total/len(self.valores)

    #Funcion para contar las consonantes
    def ContarConsonantes(self):
        cant = 0
        for a  in self.valores:
            if a not in ['a','e','i','o','u']:
                cant += 1
    
        return cant

    #Funcion para contar las vocales
    def ContarVocales(self):
        cant = 0
        for a  in self.valores:
            if a in ['a','e','i','o','u']:
                cant += 1
    
        return cant