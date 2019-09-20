from Contratos.Venda import Venda
from Contratos.Aluguel import Aluguel


class GerirContratos(object):
  def __init__(self, ano):
    self.ano = ano 
    self.contratos = list()
  
  def saveContract(self, contrato):
    self.contratos.append(contrato)
    pass
  
  def getContracts(self):
    return self.contratos

  def getInformations(self):
    n_vendas = 0
    for contract in self.contratos:
      if contract.getTipo() == "Venda":
        n_vendas = 1 + n_vendas
    print(f""" Base de dados dos contratos do ano de {self.ano}
    Foram no total de {n_vendas} Vendas e {len(self.contratos) - n_vendas} imoveis alugados. """)

  def getContractSale(self):
    print(f''' Lista de contratos de vendas de {self.ano} ''')
    print('Locador'.center(15) +"|"+"Locatario".center(15)+"|"+"Valor".center(15))
    for contract in self.contratos:
      if (contract.getTipo() == 'Venda'):
        print(f"{contract.getLocador().getNome()}".center(15)+"|"+ f"{contract.getLocatario().getNome()}".center(15)+"|"+f"{contract.getValor()}".center(15))
    return

  def getContractRent(self):
    print(f''' Lista de contratos de alugueis de {self.ano} ''')
    print('Locador'.center(15) +"|"+"Locatario".center(15)+"|"+"Valor".center(15))
    for contract in self.contratos:
      if (contract.getTipo() != 'Venda'):
        print(f"{contract.getLocador().getNome()}".center(15)+"|"+ f"{contract.getLocatario().getNome()}".center(15)+"|"+f"{contract.getValorParcela()}".center(15))
    return