from Contratos.Venda import Venda
from Contratos.Aluguel import Aluguel
from Interfaces.Iterator import Iterator

class GerirContratos(Iterator):
  def __init__(self, ano):
    Iterator.__init__(self)
    self.ano = ano 
    self.contratos = list()
    self.key = 0
  
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

  def key(self):
    return self.key

  def nextt(self):
    self.key += 1
    pass

  def rewind(self):
    self.key = 0
    pass

  def current(self):
    try:
      return self.contratos[self.key].key
      pass
    except:
      return 'Não há mais itens na lista!'
      pass
    

  def count(self):
    return len(self.contratos)

  def remove(self, key):
    for index in range(0, self.count()):
      if self.contratos[index].key == key:
        self.contratos.pop(index)
        print(f'Contrato {key} excluido!')
        break
    else:
      print ('Contrato nao localizado')