from Builder.ImovelBuilder import ImovelBuilder

class ImobiliariaDirector(object):
  def __init__(self, imovel):
    self.meuImovel = imovel
    pass
 
  def construct(self, donoImovel):
    self.meuImovel.buildDadosImovel()
    self.meuImovel.buildProprietario(donoImovel)
    self.meuImovel.buildLocalizacao()
    self.meuImovel.buildTerreno()
    self.meuImovel.buildValor()

  def getImovel(self):
    return self.meuImovel.getImovel()
    
