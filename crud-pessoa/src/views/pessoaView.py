from ..controllers.pessoa_controller import PessoaController
from ..models.pessoas import Pessoa

"""
    View responsável por adicionar, remover, atualizar e listar pesssoas.
"""

def adicionarPessoa():
    cpf = input("Digite o cpf da pessoa:")
    if (verificaCPF(cpf) == 1):
        print(' \n CPF informado já cadastrado!')
    else:
        nome = input("Digite o nome da pessoa:")
        sobrenome = input("Digite o sobrenome da pessoa:")
        data_de_nascimento = input("Digite a data de nascimento da pessoa:")

        nova_pessoa = Pessoa(nome = nome,sobrenome = sobrenome, cpf = cpf, data_de_nascimento = data_de_nascimento )
        PessoaController.salvar_pessoa(nova_pessoa)
        print(' \n ----  Cadastro realizado com sucesso! ----')

def buscarPessoa():
    cpf = input('Digite o CPF da pessoa: ')
    for pessoa in PessoaController.listar_pessoas():
        if (pessoa.cpf == cpf):
            return print(f' Nome: {pessoa.nome} \n Sobrenome: {pessoa.sobrenome} \n CPF: {pessoa.cpf} \n Data de Nascimento: {pessoa.data_de_nascimento}')
        else:
            return print('\n CPF da pessoa informada não possui cadastro.')

def atualizarPessoa():
   cpf = input('Digite o CPF da pessoa:')
   for pessoa in PessoaController.listar_pessoas():
       if (pessoa.cpf == cpf):
           novoNome = input('Digite o novo nome da pessoa:')
           novoSobrenome = input('Digite o novo sobrenome da pessoa:')
           pessoa.nome = novoNome
           pessoa.sobrenome = novoSobrenome
           return print('\n Dados atualizados com sucesso!')
       else:
           return print('\n CPF da pessoa informada não possui cadastro.')


def listarPessoas():
    if not PessoaController.listar_pessoas():
        print('\n Não possui cadastro de nenhuma pessoa no momento!')
    else:
        for pessoa in PessoaController.listar_pessoas():
            print(' ------------------------ ')
            print(f' Nome: {pessoa.nome} \n Sobrenome: {pessoa.sobrenome} \n CPF: {pessoa.cpf} \n Data de Nascimento: {pessoa.data_de_nascimento}')

def removerPessoa():
    cpf = input('Digite o CPF da pessoa: ')
    for pessoa in PessoaController.listar_pessoas():
        if (pessoa.cpf == cpf):
            PessoaController.remover_pessoa(pessoa)
            return print(f'\n CPF: {pessoa.cpf} foi removido com sucesso!')
        else:
            return print('\n CPF da pessoa informada não possui cadastro.')

def verificaCPF(cpf):
    for i in PessoaController.listar_pessoas():
        if (i.cpf == cpf):
            return 1
        else:
            return 0
