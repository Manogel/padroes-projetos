from Cart import Cart
from Product import Item
from Flyweight.FlyweightFactory import ProductFactory

orcamento = Cart()


productFactory = ProductFactory()
productFactory.make('Arroz', 3)
productFactory.make('Feijao', 6)
productFactory.make('Feijao', 7)
productFactory.make('Arroz', 3)
productFactory.make('Feijao', 7)
orcamento.adiciona_item(Item("Abacate", 100.0))
orcamento.adiciona_item(Item("Cebola", 50.0))
orcamento.adiciona_item(Item("Alho", 400.0))

print(orcamento.valor)

orcamento.aprova()

orcamento.aplica_desconto_extra(0.5)

print(orcamento.valor)

orcamento.finaliza()