from Classe import*


def Main_menu():
    print('''
1 - Criar cachorro
2 - Criar humano
3 - Listar cachorro
4 - Listar humano
5 - Excluir cachorro
6 - Excluir humano
7 - Sair''')
    

def Mostrar_cachorro():
    nome = input("Nome do cachorro: ")
    tamanho = input("Tamanho do cachorro: ")
    raca = input("Raça do cachorro: ")
    

def Mostrar_humano():
    nome = input("Nome: ")
    idade = input("Idade: ")
    tamanho = input("Tamanho:")
    sexo = input("Sexo: ")
    cor = input("Cor: ")

def Listar_cachorro():
    num =1
    for cao in Cachorro.lista_cachorro:
        print(f"Nome do cachorro na posição {num}°: {cao.nome}")
        num +=1

def Listar_humano():
    num =1
    for humano in Humano.lista_humano:
        print(f"Nome do humano na posição {num}°: {humano.nome}")
        num +=1

def Ecluir_cachorro():
    nome = input('Digite o nome do cachorro: ')
    i=0
    for cao in Cachorro.lista_cachorro:
        if nome == cao.nome:
            Cachorro.lista_cachorro.pop(i)
            print("O cachorro foi deletado")
        i+=1

def Ecluir_humano():
    nome = input('Digite o nome do humano: ')
    i=0
    for humano in Humano.lista_humano:
        if nome == humano.nome:
            Humano.lista_humano.pop(i)
            print("O humano foi deletado")
        i+=1
    
    
            
    
    
# def saida():
#     pass

# def Listar_humano():