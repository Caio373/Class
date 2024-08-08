from Classe import *
lista_cachorro = []
lista_humano = []

def criar_cao():
    nome = input("Nome do cachorro: ")
    tamanho = input("Tamanho do cachorro: ")
    raca = input("Raça do cachorro: ")
    cao = Cachorro(nome, tamanho, raca)
    lista_cachorro.append(cao)
    
    

def criar_humano():
    nome = input("Nome: ")
    sexo = input("Sexo: ")
    cor = input("Cor: ")
    humano = Humano(nome, sexo, cor)
    lista_humano.append(humano)

def Listar(lista):
    if len(lista) > 0:
        for objeto in lista:
            print(objeto.info())
    else:
        print("Lista vazia")