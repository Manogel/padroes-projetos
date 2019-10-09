from Cart import Cart
from Product import Item


orcamento = Cart()

orcamento.adiciona_item(Item("Abacate", 100.0))
orcamento.adiciona_item(Item("Cebola", 50.0))
orcamento.adiciona_item(Item("Alho", 400.0))

print(orcamento.valor)

orcamento.aprova()

orcamento.aplica_desconto_extra(0.5)

print(orcamento.valor)

orcamento.finaliza()