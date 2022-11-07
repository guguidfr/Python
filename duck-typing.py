class pato: # Objeto
    def hablar(self): # Método
        print("¡Cua, cua!")
class perro:
    def hablar(self):
        print("¡Guau, Guau!")
class gato:
    def hablar(self):
        print("¡Miau, Miau!")
class vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")
def llama_hablar(x):
    x.hablar()
        
p = pato()
p.hablar()

llama_hablar(p)
llama_hablar(perro())
llama_hablar(gato())
llama_hablar(vaca())