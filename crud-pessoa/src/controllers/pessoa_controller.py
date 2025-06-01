from models.pessoas import Pessoa
from database import db

class PessoaController:
    @staticmethod
    def salvar_pessoa(nome, sobrenome, cpf, data_nascimento):
        pessoa = Pessoa(nome=nome, sobrenome=sobrenome, 
                       cpf=cpf, data_de_nascimento=data_nascimento)
        db.session.add(pessoa)
        db.session.commit()
    
    @staticmethod
    def listar_pessoas():
        return Pessoa.query.all()
    
    @staticmethod
    def remover_pessoa(pessoa):
        db.session.delete(pessoa)
        db.session.commit()