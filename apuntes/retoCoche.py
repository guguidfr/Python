"""
Si el depósito del coche es mayor a 0, arranca. Si no, no.
"""
class coche():
    def tanque(self):
        tanque = int(input("¿Cuántos litros tiene el tanque? "))
        if tanque <=0:
            print("No nos vamos")
        else:
            print("Vamonos")
c = coche()
c.tanque()