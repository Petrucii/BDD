from pytest_bdd import scenarios, given, when, then, parsers

from carrinho import criar_carrinho, adicionar_produto

scenarios("carrinho.feature")


@given("que o carrinho está vazio", target_fixture="carrinho")
def carrinho_vazio():
    return criar_carrinho()


@given(
    parsers.parse("que o estoque disponível é de {estoque:d} unidades"),
    target_fixture="estoque",
)
def estoque_disponivel(estoque):
    return estoque


@when(
    parsers.parse(
        "eu tento adicionar {quantidade:d} unidades de um produto que custa {preco:d} reais"
    )
)
def tentar_adicionar(carrinho, estoque, quantidade, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as e:
        carrinho["erro"] = str(e)


@then(parsers.parse("o carrinho deve conter {itens:d} itens"))
def valida_itens(carrinho, itens):
    assert carrinho["itens"] == itens


@then(parsers.parse("o total do carrinho deve ser {total:d} reais"))
def valida_total(carrinho, total):
    assert carrinho["total"] == total


@then(parsers.parse('o sistema deve exibir o erro "{mensagem}"'))
def valida_erro(carrinho, mensagem):
    assert carrinho.get("erro") == mensagem