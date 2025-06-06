def funzione_doppio(x):
    """Questa funzione restituisce il doppio del argomento passato alla funzione"""
    return x*2

def funzione_quadrato(y):
   return y*y

class ClasseParzialmenteImplementata:
    def __init__(self, nome):
        self.nome = nome

    def metodo_esistente(self):
        return f"Ciao, sono {self.nome}!"

    def metodo_da_completare(self, valore:str):
        return self.nome + valore