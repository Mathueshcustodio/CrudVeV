from flask import Flask, render_template, request, redirect, url_for, flash
from models.pessoas import Pessoa
from controllers.pessoa_controller import PessoaController
from database import db, init_app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.db'
import secrets
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Gera uma chave segura
#app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

# Inicializa o banco de dados
init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
#função para cadastrar usuario
def cadastrar_pessoa():
    if request.method == 'POST':
        try:
            PessoaController.salvar_pessoa(
                request.form['nome'],
                request.form['sobrenome'],
                request.form['cpf'],
                request.form['data_de_nascimento']
            )
            flash('Pessoa cadastrada com sucesso!', 'success')
            return redirect(url_for('listar_pessoas'))
        except Exception as e:
            flash(f'Erro ao cadastrar: {str(e)}', 'danger')
    return render_template('cadastrar.html')

@app.route('/listar')
#função para listar usuario
def listar_pessoas():
    pessoas = Pessoa.query.all()
    return render_template('listar.html', pessoas=pessoas)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])

#função para editar usuario
def editar_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    if request.method == 'POST':
        try:
            pessoa.nome = request.form['nome']
            pessoa.sobrenome = request.form['sobrenome']
            pessoa.cpf = request.form['cpf']
            pessoa.data_de_nascimento = request.form['data_nascimento']
            db.session.commit()
            flash('Pessoa atualizada com sucesso!', 'success')
            return redirect(url_for('listar_pessoas'))
        except Exception as e:
            flash(f'Erro ao atualizar: {str(e)}', 'danger')
    return render_template('editar.html', pessoa=pessoa)

@app.route('/remover/<int:id>')

# função para remover usuario
def remover_pessoa(id):
    try:
        pessoa = Pessoa.query.get_or_404(id)
        db.session.delete(pessoa)
        db.session.commit()
        flash('Pessoa removida com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao remover: {str(e)}', 'danger')
    return redirect(url_for('listar_pessoas'))

if __name__ == '__main__':
    app.run(debug=True)