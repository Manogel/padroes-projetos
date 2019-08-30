# -*- coding: utf-8 -*-
from Imoveis.Galpao import Galpao
from Imoveis.Residencia import Residencia
#from Contratos.Venda import Venda
#from Contratos.Aluguel import Aluguel
from Pessoas.Locador import Locador
from Pessoas.Locatario import Locatario
from Contratos.GeraContrato import GeraContrato

#novoLocador = Locador('Manoel',  '30-10-1999', '03951567260', 'Brasileiro', '68925153', '781', '96991934171', 'manoelgomes53@gmail.com')

#novoGalpao = Galpao(float(2.999), "Area de lazer", '68925153', '781', float(59.76), float(80.89))
#novoGalpao.getInformation()

#novaCasa = Residencia(novoLocador, "Apartamento", float(2999), "Area de lazer", '68925153', '781', float(59.76), float(80.89), 1, 2, 3, 4)
#novaCasa.getInformation()

#print(novoGalpao.cidade)

#novoLocatario = Locatario('Gustavo',  '30-10-1996', '03951567260', 'Brasileiro', '68903770', '781', '96991934171', 'manoelgomes53@gmail.com', "42443232324")
#novoLocatario.dadosPessoa()

#novoContrato = Venda(novaCasa, novoLocador, novoLocatario, '10-10-2019', '10-10-2020', 'Vendedor pagou em cheque', float(1000))
#novoContrato = Aluguel(novaCasa, novoLocador, novoLocatario, '10-10-2019', '10-10-2020', 'Vendedor pagou em cheque', float(1500), 10)
#novoContrato.imprimirContrato()

contrato = GeraContrato.montaContrato("Aluguel", '10-10-2019', '10-10-2020', 'Vendedor pagou em cheque', float(1500), 10)
if(contrato != None):
  contrato.imprimirContrato()
else:
  print('Não foi gerado nenhum contrato!')