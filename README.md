# MARCOS HENRIQUE PETRUCI 2502570

# Carrinho de Compras com BDD

Exercício prático de **BDD (Behavior-Driven Development)** em Python, usando `pytest` e `pytest-bdd`.

## O que o sistema faz

Um carrinho de compras básico em que o cliente adiciona produtos e vê o valor total atualizado. Se a quantidade desejada for maior que o estoque disponível, o sistema levanta o erro **"Estoque insuficiente"**.

## Estrutura

| Arquivo | Descrição |
|---|---|
| `carrinho.feature` | Cenários em Gherkin (em português) com o comportamento esperado |
| `carrinho.py` | Regra de negócio: `criar_carrinho()` e `adicionar_produto()` |
| `test_carrinho.py` | Testes automatizados que ligam o Gherkin ao código Python |

## Cenários

1. **Adicionar um produto com sucesso** (há estoque suficiente): o carrinho passa a ter os itens e o total correto.
2. **Tentar adicionar sem estoque suficiente**: o sistema exibe o erro "Estoque insuficiente" e o carrinho permanece inalterado.

## Como executar

Pré-requisito: Python 3 instalado.

```bash
pip install pytest pytest-bdd
pytest test_carrinho.py -v
```

Se aparecer `ModuleNotFoundError: pytest_bdd`, o `pytest` está usando outro Python. Rode com:

```bash
python -m pytest test_carrinho.py -v
```

Resultado esperado:

```
test_carrinho.py::test_adicionar_um_produto_com_sucesso_quando_há_estoque_suficiente PASSED
test_carrinho.py::test_tentar_adicionar_um_produto_sem_estoque_suficiente PASSED
```

## Observações

- O arquivo `carrinho.feature` deve ficar na mesma pasta de `test_carrinho.py`.
- A primeira linha do `.feature` (`# language: pt`) é necessária para o pytest-bdd entender as palavras-chave em português (Funcionalidade, Cenário, Dado, Quando, Então, E).
- No passo `@when`, o `ValueError` é capturado com `try/except` e guardado em `carrinho["erro"]`, para que o passo `@then` possa validar a mensagem.
