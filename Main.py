from Classe import*
from Views import*
from Functions import*


# def criar_cao():
#     nome = input("Nome do cachorro: ")
#     tamanho = input("Tamanho do cachorro: ")
#     raca = input("Raça do cachorro: ")
#     cao = Cachorro(nome, tamanho, raca)
#     Cachorro.cachorros.append(cao)
    
    

# def criar_humano():
#     nome = input("Nome: ")
#     sexo = input("Sexo: ")
#     cor = input("Cor: ")
#     humano = Humano(nome, sexo, cor)
#     Humano.humanos.append(humano)

# def Listar(lista):
#     for objeto in lista:
#         print(objeto.info())

while True:
    Main_menu()
    op = int(input("Digite a opção: "))
    if 1 == op:
        criar_cao()

    if 2 == op:
        criar_humano()

    if 3 == op:
        Listar_cachorro()

    if 4 == op:
        Listar_humano()

    if 5 == op:
        Ecluir_cachorro()
        

    if 6 == op:
        Ecluir_humano()

    
    if 7 == op:
        break
       