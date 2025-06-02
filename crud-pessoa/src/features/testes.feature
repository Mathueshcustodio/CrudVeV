#language: pt

Funcionalidade: Gerenciamento de pessoas
  Como usuário do sistema
  Quero cadastrar, listar, editar e remover pessoas
  Para manter o controle dos registros

  Cenário: Cadastrar uma nova pessoa com sucesso
    Dado que o sistema está funcionando
    Quando eu enviar os dados de uma nova pessoa válidos
    Então a pessoa deve ser cadastrada com sucesso

  Cenário: Listar todas as pessoas cadastradas
    Dado que existem pessoas cadastradas no sistema
    Quando eu acessar a página de listagem de pessoas
    Então o sistema deve exibir todas as pessoas cadastradas

  Cenário: Editar os dados de uma pessoa existente - FALHOU
    Dado que existe uma pessoa cadastrada com CPF "12345678900"
    Quando eu alterar o nome dessa pessoa para "JoAo Atualizado"
    Então os dados da pessoa devem ser atualizados com sucesso
    E a nova informação deve aparecer na listagem

  Cenário: Remover uma pessoa existente
    Dado que existe uma pessoa cadastrada com CPF "98765432100"
    Quando eu solicitar a remoção dessa pessoa
    Então a pessoa deve ser removida com sucesso

  Cenário: Tentar cadastrar uma pessoa com CPF duplicado - FALHOU
    Dado que já existe uma pessoa com CPF "11122233344" cadastrada
    Quando eu tentar cadastrar outra pessoa com o mesmo CPF
    Então o sistema deve exibir uma mensagem de erro
    E a pessoa não deve ser cadastrada
