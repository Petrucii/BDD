# language: pt
Funcionalidade: Carrinho de compras
  Como cliente do e-commerce
  Quero adicionar produtos ao meu carrinho
  Para ver o valor total atualizado, sem exceder o estoque disponível

  Cenário: Adicionar um produto com sucesso quando há estoque suficiente
    Dado que o carrinho está vazio
    E que o estoque disponível é de 10 unidades
    Quando eu tento adicionar 3 unidades de um produto que custa 50 reais
    Então o carrinho deve conter 3 itens
    E o total do carrinho deve ser 150 reais

  Cenário: Tentar adicionar um produto sem estoque suficiente
    Dado que o carrinho está vazio
    E que o estoque disponível é de 2 unidades
    Quando eu tento adicionar 5 unidades de um produto que custa 50 reais
    Então o sistema deve exibir o erro "Estoque insuficiente"
    E o total do carrinho deve ser 0 reais
    E o carrinho deve conter 0 itens
