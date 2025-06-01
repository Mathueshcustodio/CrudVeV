from .pessoaView import *

"""
    View responsável pela tela principal da aplicação.
"""

# ------------------------------------------------
#  Menu de navegação
# ------------------------------------------------

menu  = """
    ---- Sistema de CRUD em Python -----

    [c] - Cadastrar pessoa
    [b] - Buscar pessoa
    [a] - Atualizar pessoa
    [l] - Listar pessoas
    [d] - Deletar pessoa
    [q] - Sair do sistema

"""
def menu_navegacao():

    while True:
        opcao = input(menu)

        match opcao:

            case 'c':
                adicionarPessoa() 
            case 'b':
                buscarPessoa()
            case 'a':
                atualizarPessoa()
            case 'l':
                listarPessoas()
            case 'd':
                removerPessoa()
            case 'q':
                print('=== Finalizando sistema... ====')
                exit()
            case _:
                print("Opção inválida!") 

    

