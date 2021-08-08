class Animal():
    total_recorrido = 0
    apodo = None

    def caminar(self):
        self.total_recorrido = self.total_recorrido + self.velocidad
        print(f'El {self.nombre} llamado {self.apodo} se ha movido {self.velocidad}, acumulando una distancia recorrida de {self.total_recorrido}')

    def comer(self):
        pass

    def __init__(self, apodo):
        self.apodo = apodo

class Gato(Animal):
    nombre = 'Gato'
    velocidad = 2
    # def __init__(self, apodo):
    #     self.apodo = apodo

class CabashoQueSeCreeHumano(Animal):
    nombre = 'Cabasho'
    apodo = None
    velocidad = 10
    
    # def __init__(self, apodo):
    #     self.apodo = apodo
