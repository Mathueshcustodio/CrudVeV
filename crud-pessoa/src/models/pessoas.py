from database import db

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_de_nascimento = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Pessoa {self.nome} {self.sobrenome}>'