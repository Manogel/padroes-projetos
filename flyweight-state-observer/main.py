from Cart import Cart
from Product import Item
from Flyweight.FlyweightFactory import ProductFactory
from observadores import imprime, envia_email, salvar
from nota import Nota_fiscal
from datetime import date

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
# print(orcamento.obter_itens())

nota_fiscal = Nota_fiscal(
        razao_social='MAnogel',
        cnpj='01928391827321',
        itens=orcamento.obter_itens(),
        data_de_emissao=date.today(),
        detalhes='',
        observadores=[imprime, envia_email, salvar]
)