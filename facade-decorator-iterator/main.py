# -*- coding: utf-8 -*-
from Imoveis.Galpao import Galpao
from Imoveis.Residencia import Residencia
from Contratos.Venda import Venda
from Contratos.Aluguel import Aluguel
from Pessoas.Locador import Locador
from Pessoas.Locatario import Locatario
from Contratos.GerirContratos import GerirContratos
from Facade.index import Facade


lista_contratos = GerirContratos('2019')
locador = Locador()

locador.setDataLocalization('68925153', '781')
locador.setUserInformation('Manoel', '30-10-1999', '03951567260',
                           'Brasileiro', '96991934171', 'manoelgomes53@gmail.com')


interface = Facade()
Imovel1 = interface.newImovel('Casa Gernimana')
Imovel1.getInformation()


Contrato_venda = Venda(Imovel1, locador)
Contrato_venda.setValor(float(222))
lista_contratos.saveContract(Contrato_venda)


Contrato_aluguel = Aluguel(Imovel1, locador)
Contrato_aluguel.setValorParcela(float(222))

lista_contratos.saveContract(Contrato_aluguel)

# Contrato_aluguel.imprimirImovelContrato()
# Contrato_venda.imprimirImovelContrato()
print(lista_contratos.current())
lista_contratos.nextt()
lista_contratos.remove('1ADF2')
print(lista_contratos.current())
lista_contratos.nextt()
print(lista_contratos.current())
