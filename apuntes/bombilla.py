import random
class bombilla():
    estados = ("Encendida","Apagada")
    estado = random.choice(estados)
    def encender(self):
        estado = "Encendida"
        print(estado)
    def apagar(self):
        estado = "Apagada"
        print(estado)
bombilla().encender()