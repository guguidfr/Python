"""
Tenemos el objeto 'bombilla', que no sabemos en qué estado está y queremos cambiar su estado
"""
import random
class bombilla():
    def estado(cambio):
        estados = ("Encendido", "Apagado")
        estado = random.choice(estados)
        if cambio == 1 and estado == "Encendido":
            estado = "Apagado"
        elif cambio == 1 and estado == "Apagado":
            estado = "Encendido"
        print(estado)
objeto = bombilla()
objeto.estado()