# -*- coding: utf-8 -*-
from Imoveis.Galpao import Galpao
from Imoveis.Residencia import Residencia
from Contratos.Venda import Venda
from Contratos.Aluguel import Aluguel
from Pessoas.Locador import Locador
from Pessoas.Locatario import Locatario
from Contratos.GerirContratos import GerirContratos


lista_contratos = GerirContratos('2019')
locador = Locador('Manoel',  '30-10-1999', '03951567260', 'Brasileiro', '68925153', '781', '96991934171', 'manoelgomes53@gmail.com')
locatario = Locatario('Gustavo',  '30-10-1996', '03951567260', 'Brasileiro', '68903770', '781', '96991934171', 'manoelgomes53@gmail.com', "42443232324")

Imovel1 = Galpao(locador, float(2.999), "Area de lazer", '68925153', '781', float(59.76), float(80.89))
#Imovel1.getInformation()

Imovel2 = Residencia(locador, "Casa Geminada", float(2999), "Area de lazer", '68925153', '781', float(59.76), float(80.89), 1, 2, 3, 4)
#Imovel2.getInformation()

Contrato_venda = Venda(Imovel1, locador, locatario)
Contrato_venda.setValor(float(222))
lista_contratos.saveContract(Contrato_venda)

#print(Contrato_venda.getValor())

copia = Contrato_venda.clonar()
copia.setValor(33.389)
lista_contratos.saveContract(copia)
#print(copia.getValor())
#copia.imprimirContrato()

Contrato_aluguel = Aluguel(Imovel1, locador, locatario)
Contrato_aluguel.setValorParcela(float(222))

lista_contratos.saveContract(Contrato_aluguel)
#copia2.imprimirContrato()
#print(Contrato_aluguel.getValorParcela())

copia2 = Contrato_aluguel.clonar()
copia2.setValorParcela(float(2862))
lista_contratos.saveContract(copia2)

#copia2.imprimirContrato()

lista_contratos.getInformations()
lista_contratos.getContractSale()
lista_contratos.getContractRent()