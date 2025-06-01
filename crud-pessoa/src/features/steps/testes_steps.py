from behave import given, when, then
from app import app
from database import db
from models.pessoas import Pessoa

@given('que o sistema está funcionando')
def step_impl(context):
    context.client = app.test_client()

@when('eu enviar os dados de uma nova pessoa válidos')
def step_impl(context):
    data = {
        'nome': 'Joana',
        'sobrenome': 'Duarte',
        'cpf': '12345678900',
        'data_de_nascimento': '1990-01-01'
    }
    context.response = context.client.post('/cadastrar', data=data, follow_redirects=True)

@then('a pessoa deve ser cadastrada com sucesso')
def step_impl(context):
    response_text = context.response.get_data(as_text=True)
    print(response_text)  # Debug, remova depois
    assert 'Pessoa cadastrada com sucesso!' in response_text

@given('que existem pessoas cadastradas no sistema')
def step_impl(context):
    with app.app_context():
        db.drop_all()
        db.create_all()
        pessoas = [
            Pessoa(nome='Carlos', sobrenome='Campos', cpf='11111111111', data_de_nascimento='1992-02-19'),
            Pessoa(nome='Ruth', sobrenome='Xavier', cpf='22222222222', data_de_nascimento='1997-01-15')
        ]
        db.session.bulk_save_objects(pessoas)
        db.session.commit()

@when('eu acessar a página de listagem de pessoas')
def step_impl(context):
    context.response = context.client.get('/listar')

@then('o sistema deve exibir todas as pessoas cadastradas')
def step_impl(context):
    response_text = context.response.get_data(as_text=True)
    assert 'Carlos' in response_text
    assert 'Ruth' in response_text

@given('que existe uma pessoa cadastrada com CPF "12345678900"')
def step_impl(context):
    with app.app_context():
        db.drop_all()
        db.create_all()
        pessoa = Pessoa(nome='Maria', sobrenome='Silva', cpf='12345678900', data_de_nascimento='1985-05-20')
        db.session.add(pessoa)
        db.session.commit()

@when('eu alterar o nome dessa pessoa para "{novo_nome}"')
def step_impl(context, novo_nome):
    with app.app_context():
        pessoa = Pessoa.query.filter_by(cpf='12345678900').first()
        data = {
            'nome': novo_nome,
            'sobrenome': pessoa.sobrenome,
            'cpf': pessoa.cpf,
            'data_de_nascimento': pessoa.data_de_nascimento
        }
        context.response = context.client.post(f'/editar/{pessoa.id}', data=data, follow_redirects=True)

@then('os dados da pessoa devem ser atualizados com sucesso')
def step_impl(context):
    response_text = context.response.get_data(as_text=True)
    print(response_text)  # Debug, remova depois
    assert 'Pessoa atualizada com sucesso!' in response_text

@then('a nova informação deve aparecer na listagem')
def step_impl(context):
    context.response = context.client.get('/listar')
    response_text = context.response.get_data(as_text=True)
    # Atenção: João com til (~) e letra maiúscula
    assert 'João Atualizado' in response_text

@given('que existe uma pessoa cadastrada com CPF "98765432100"')
def step_impl(context):
    with app.app_context():
        db.drop_all()
        db.create_all()
        pessoa = Pessoa(nome='Carlos', sobrenome='Ferreira', cpf='98765432100', data_de_nascimento='1980-03-03')
        db.session.add(pessoa)
        db.session.commit()

@when('eu solicitar a remoção dessa pessoa')
def step_impl(context):
    with app.app_context():
        pessoa = Pessoa.query.filter_by(cpf='98765432100').first()
        context.response = context.client.get(f'/remover/{pessoa.id}', follow_redirects=True)

@then('a pessoa deve ser removida com sucesso')
def step_impl(context):
    response_text = context.response.get_data(as_text=True)
    print(response_text)  # Debug, remova depois
    assert 'Pessoa removida com sucesso!' in response_text

@given('que já existe uma pessoa com CPF "11122233344" cadastrada')
def step_impl(context):
    with app.app_context():
        db.drop_all()
        db.create_all()
        pessoa = Pessoa(nome='Pedro', sobrenome='Almeida', cpf='11122233344', data_de_nascimento='1988-11-11')
        db.session.add(pessoa)
        db.session.commit()

@when('eu tentar cadastrar outra pessoa com o mesmo CPF')
def step_impl(context):
    data = {
        'nome': 'Pedro Duplicado',
        'sobrenome': 'Almeida',
        'cpf': '11122233344',
        'data_de_nascimento': '1990-11-11'
    }
    context.response = context.client.post('/cadastrar', data=data, follow_redirects=True)

@then('o sistema deve exibir uma mensagem de erro')
def step_impl(context):
    response_text = context.response.get_data(as_text=True)
    print(response_text)  # Debug, remova depois
    # Verifique se a mensagem no seu código é com acento ou sem
    assert 'CPF já cadastrado!' in response_text or 'CPF ja cadastrado!' in response_text

@then('a pessoa não deve ser cadastrada')
def step_impl(context):
    with app.app_context():
        pessoas = Pessoa.query.filter_by(cpf='11122233344').all()
        assert len(pessoas) == 1
