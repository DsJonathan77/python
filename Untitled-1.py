class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]

def reverter_string(texto):
    pilha = Pilha()
    
    # Empilha cada caractere da string
    for caractere in texto:
        pilha.empilhar(caractere)
    
    # Desempilha formando a string invertida
    invertida = ''
    while not pilha.esta_vazia():
        invertida += pilha.desempilhar()
    
    return invertida

