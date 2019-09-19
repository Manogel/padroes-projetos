from Builder.Imovel import ImovelProduct
from abc import ABC, abstractmethod

class ImovelBuilder(ABC):
  def __init__(self):
    self.imovel = ImovelProduct()
    pass

  def getImovel(self):
    return self.imovel

  @abstractmethod 
  def buildProprietario(self):
    pass

  @abstractmethod 
  def buildLocalizacao(self):
    pass

  @abstractmethod 
  def buildTerreno(self):
    pass

  @abstractmethod 
  def buildDadosImovel(self):
    pass

  @abstractmethod 
  def buildValor(self):
    pass

  