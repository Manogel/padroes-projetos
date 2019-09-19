# -*- coding: utf-8 -*-
from Imoveis.Galpao import Galpao
from Imoveis.Residencia import Residencia
from Contratos.Venda import Venda
from Contratos.Aluguel import Aluguel
from Pessoas.Locador import Locador
from Pessoas.Locatario import Locatario

locador = Locador('Manoel',  '30-10-1999', '03951567260', 'Brasileiro', '68925153', '781', '96991934171', 'manoelgomes53@gmail.com')
locatario = Locatario('Gustavo',  '30-10-1996', '03951567260', 'Brasileiro', '68903770', '781', '96991934171', 'manoelgomes53@gmail.com', "42443232324")

Imovel1 = Galpao(locador, float(2.999), "Area de lazer", '68925153', '781', float(59.76), float(80.89))
#novoGalpao.getInformation()

Imovel2 = Residencia(locador, "Casa Geminada", float(2999), "Area de lazer", '68925153', '781', float(59.76), float(80.89), 1, 2, 3, 4)
#novaCasa.getInformation()

Contrato = Venda('10-10-2019', '10-10-2020', "Pagou em cheque")
Contrato.setImovel(Imovel1)
Contrato.setLocador(locador)
Contrato.setLocatario(locatario)
Contrato.imprimirContrato()

print("=============||==============")

Contrato = Venda('10-10-2019', '10-10-2020', "Pagou em dinheiro")
Contrato.setImovel(Imovel2)
Contrato.setLocador(locador)
Contrato.setLocatario(locatario)
Contrato.imprimirContrato()

print("=============||==============")

Contrato = Aluguel('10-10-2019', '10-10-2020', "Pagou em deposito")
Contrato.setImovel(Imovel1)
Contrato.setLocador(locador)
Contrato.setLocatario(locatario)
Contrato.imprimirContrato()

print("=============||==============")

Contrato = Aluguel('10-10-2019', '10-10-2020', "Pagou em cheque")
Contrato.setImovel(Imovel2)
Contrato.setLocador(locador)
Contrato.setLocatario(locatario)
Contrato.imprimirContrato()

#print(novoGalpao.cidade)

#novoLocatario = Locatario('Gustavo',  '30-10-1996', '03951567260', 'Brasileiro', '68903770', '781', '96991934171', 'manoelgomes53@gmail.com', "42443232324")
#novoLocatario.dadosPessoa()

#novoContrato = Venda(novaCasa, novoLocador, novoLocatario, '10-10-2019', '10-10-2020', 'Vendedor pagou em cheque', float(1000))
#novoContrato = Aluguel(novaCasa, novoLocador, novoLocatario, '10-10-2019', '10-10-2020', 'Vendedor pagou em cheque', float(1500), 10)
#novoContrato.imprimirContrato()

