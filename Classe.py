class Animal:
    nome = str
    coracao: bool
    menbros = bool
    sexo = True
    tamanho = int
    
    def __init__(self, nome,menbros,tamanho):
        self.nome = nome
        self.coracao = True
        self.menbros = menbros
        self.sexo = True
        self.tamanho = tamanho

class Humano(Animal):
    lista_humano = []
    racionalidade: bool
    cor: str

    def __init__(self, nome,sexo,cor):
        self.nome = nome
        self.coracao = True
        self.menbros = True
        self.sexo = sexo
        self.tamanho = int
        self.cor = cor
        


    pass


class Cachorro(Animal):
    lista_cachorro = []
    tamanho:0
    cor:str
    
    
    def __init__(self,nome, tamanho, raca):
        super().__init__(nome,True,True)
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.coracao = True
        