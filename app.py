import os

restaurantes = ['Pizza','Sushi',]

def exibir_nome_do_programa():
    print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print ('1. Cadastar restaurante')
    print ('2. Listar restaurante')
    print ('3. Ativar restaurante')
    print ('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')   

def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    #lista.função(dado que será adicionado)
    #append é usado para colocar na lista um novo dado
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
    
def Listar_restaurante():
    os.system('cls')
    print('Listando os restaurantes\n')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
                            #prefixo int para colocar a string em numero inteiro

            #print(f'Você escolheu a opção{opcao_escolhida}')
            #interpolação de strings, uso para dentro de uma string ler uma função dentro de uma string

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            Listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
